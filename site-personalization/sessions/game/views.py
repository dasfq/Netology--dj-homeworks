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

def choose_template(request):
    if is_player_host(request):
        template = 'home.html'
    else:
        template = 'input.html'
    return template

def is_player_host(request):
    player_id = request.session['player_id']
    is_host = Player.objects.filter(id=player_id).values()[0]['is_host']
    return is_host

def is_current_game(request):
    games_list = Game.objects.all().order_by('-id')
    return request.session.get('game_id', 0) == games_list[0].id

def show_home(request):
    games_list = Game.objects.all().order_by('-id')
    if games_list.count() == 0:
        current_game = start_host_game(request)
        template_name = choose_template(request)
    else:
        latest_game_id = games_list[0].id
        current_game_id = request.session.get('game_id', latest_game_id)
        current_game = PlayerGameInfo.objects.all().get(game__id=current_game_id)
        if current_game.game.is_finished == False:
            if not is_player_exist(request):
                new_player = Player.objects.create()
                request.session['player_id'] = new_player.id
                request.session['game_id'] = current_game.game.id
            template_name = choose_template(request)
        else:
            if is_player_exist(request):
                if not is_player_host(request):
                    # тут нужно ему сообщить, что он угадал число. А во после f5 уже создать новую игру.
                    template_name = choose_template(request)
                    request.session.pop('player_id')
                    request.session.pop('game_id')
                elif is_player_host(request):
                    current_game.message = f"Число {current_game.number_hidden} было угадано c {current_game.attempt_qty} попыток."
                    template_name=choose_template(request)
                    request.session.pop('player_id')
                    request.session.pop('game_id')
            else:
                # если кто-то зайдёт без сессии, создадим новую игру и  плеера.
                current_game = start_host_game(request)
                template_name = choose_template(request)
    if request.method == 'POST':
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
    })
