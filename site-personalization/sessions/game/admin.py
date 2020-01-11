from django.contrib import admin
from .models import Game, PlayerGameInfo, Player


class GameAdmin(admin.ModelAdmin):
    pass

class PlayerAdmin(admin.ModelAdmin):
    pass

class PlayerGameInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlayerGameInfo, PlayerGameInfoAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
