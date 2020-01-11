from django.shortcuts import render, redirect
import random
from .models import Player, Game, PlayerGameInfo
from django.db import transaction


def start_host_game(request):
    number = random.randint(1, 10)
    with transaction.atomic():
        new_game = Game.objects.create(is_finished=False)
        new_player = Player.objects.create(is_host=True)
        new_game_info = PlayerGameInfo.objects.create( \
            game=new_game,
            player=new_player,
            attempt_qty=0,
            number_hidden=number,
            number_try=0)
    request.session['game_id'] = new_game.id
    request.session['player_id'] = new_player.id
    return new_game_info

def is_player_exist(request):
    return True if 'player_id' in request.session.keys() else False

def is_player_host(request):
    player_id = request.session['player_id']
    is_host = Player.objects.filter(id=player_id).values()[0]['is_host']
    if is_host:
        template = 'home.html'
    else:
        template = 'input.html'
    return template

def is_current_game(request):
    games_list = Game.objects.all().order_by('-id')
    return request.session.get('game_id', 0) == games_list[0].id

def show_home(request):
    template_name = 'home.html'
    # нужно проверять, что game_id  в сессии совпадает с текущей игрой game_id в базе
    games_list = Game.objects.all().order_by('-id')
    if games_list.count() == 0:
        # создаём новую. и записываем данные в сессию.
        print('Игр не было - создаём')
        current_game = start_host_game(request)
        template_name = is_player_host(request)
    else:
        print('Игра уже идёт')
        # Делаем последнюю созданную игру текущей.
        latest_game_id = games_list[0].id
        current_game_id = request.session.get('game_id', latest_game_id)
        current_game = PlayerGameInfo.objects.get(game__id=current_game_id)
        if current_game.game.is_finished == False:
            print('Есть незавершённая игра')
            if not is_player_exist(request):
                print('Создали нового игрока-угадывателя, т.к. у него не было сессии.')
                new_player = Player.objects.create()
                request.session['player_id'] = new_player.id
                request.session['game_id'] = current_game.game.id
            template_name = is_player_host(request)
        else:
            print('Последняя игра была завершена')
            # Если игра завершена, это может быть создатель (тогда ему покажем, что число угадано) или
            # это угадыватель. ТОгда поздравим его.
            if is_player_exist(request):
                print('Игрок существует')
                if not is_player_host(request):
                    # тут нужно ему сообщить, что он угадал число. А во 2й раз создать новую игру.
                    template_name = is_player_host(request)
                    request.session.pop('player_id')
                    print('Удалили данные из сессии у НеХоста')
                elif is_player_host(request):
                    current_game.message = f"Число {current_game.number_hidden} было угадано c {current_game.attempt_qty} попыток."
                    template_name=is_player_host(request)
                    request.session.pop('player_id')
                    request.session.pop('game_id')
                    print('Удалили данные из сессии у Хоста')
                else:
                    # если кто-то зайдёт из третьего браузера без сессии, создадим ему плеера.
                    current_game = start_host_game(request)
                    template_name = is_player_host(request)
            else:
                print('Игрок не существует. Значит создаём новую игру с игроком-хостом.')
                current_game = start_host_game(request)
                template_name = is_player_host(request)
    if request.method == 'POST':
        print('POST')
        number_try = int(request.POST.get('number_try', 0))
        if number_try < current_game.number_hidden:
            message = 'Загадано большее число'
        elif(number_try > current_game.number_hidden):
            message = 'Загадано меньшее число'
        else:
            message = 'Вы угадали, поздравляем!!! Обновите страницу, чтобы загадать новое число.'
            current_game.game.is_finished = True
            current_game.game.save()
        current_game.attempt_qty += 1
        current_game.number_try = number_try
        current_game.message = message
        current_game.save()
        return redirect('home')

    return render(request, template_name, context={
        "game": current_game,
        # "is_player_host": template_name,
    })


# как добавить ещё одного плеера к текущему объекту Game? Пробовал делать current_game.player.objects.create() - не работает. В итоге создал просто нового игрока, но он никак не связан с моей текущей игрой current_game.
# Почему то у меня совершается два GET запроса. Из-за этого вьюха запускает создание новой игры, даже если я ещё не нажал обновить страницу.