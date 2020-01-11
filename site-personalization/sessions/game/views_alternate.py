# Здесь считаю не все игры, а только незавершённые. Немного подругому будет.


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
    return is_host


def show_home(request):
    template_name = 'home.html'
    # проверяем, есть ли незавершённая игра в базе данных.
    games = Game.objects.all()
    if games.filter(is_finished=False).count() == 0:
        # создаём новую. и записываем данные в сессию.
        print('Игры не было - создаём')
        current_game = start_host_game(request)
        is_host = is_player_host(request)
    else:
        print('Незавершённая игра имеется')
        # делаем эту найденную незавершённую игру текущей.
        current_game = PlayerGameInfo.objects.get(game__is_finished=False)  # filter - queryset, get - объект
        # если человек зашёл в игру и у него ещё нет player_id  в сессии, значит он будет угадывателем и
        # создадим ему id, который запишем в сессию:

        if is_player_exist(request):
            print('Игрок существует')
            if is_player_host(request):
                print('Игрок хост, значит получит сообщение, что его число угадано')
                current_game.message = f"Число было угадано c {current_game.attempt_qty} попыток."
                current_game.player.is_host = False
                is_host = is_player_host(request)
            else:
                print('Игрок не хост, значит теперь нужно создть игру, и он должен стать хостом')
                current_game = start_host_game(request)
                is_host = is_player_host(request)
        else:
            print('Игрок не существует. Значит создаём новую игру с игроком-хостом.')
            print('Создали нового игрока-угадывателя, т.к. у него не было сессии.')
            new_player = Player.objects.create(is_host=False)
            request.session['player_id'] = new_player.id
        is_host = is_player_host(request)

    if request.method == 'POST':
        number_try = int(request.POST.get('number_try', 0))
        if number_try < current_game.number_hidden:
            message = 'Загадано большее число'
        elif (number_try > current_game.number_hidden):
            message = 'Загадано меньшее число'
        else:
            message = 'Вы угадали, поздравляем!!! Обновите страницу, чтобы загадать новое число.'
            print(f'{current_game.game.is_finished} было!')
            current_game.game.is_finished = True
            current_game.game.save()
            print(f'{current_game.game.is_finished} стало!')
        current_game.attempt_qty += 1
        current_game.number_try = number_try
        current_game.message = message
        current_game.save()
        return redirect('home')

    return render(request, template_name, context={
        "game": current_game,
        "is_player_host": is_host,
    })

