from django.db import models


class Player(models.Model):
    is_host = models.BooleanField(default=False)


class Game(models.Model):
    player = models.ManyToManyField(Player, through='PlayerGameInfo')
    is_finished = models.BooleanField(default=True)

class PlayerGameInfo(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    attempt_qty = models.IntegerField(default=0, verbose_name='Кол-во попыток')
    number_hidden = models.IntegerField(default=None, verbose_name='Загаданное число')
    number_try = models.IntegerField(default=0, verbose_name='Введённое число')
    message = models.CharField(default="", max_length=50)