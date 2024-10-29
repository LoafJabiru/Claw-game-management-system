from django.contrib import admin
from .models import Game, Player, Machine, Prize

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Machine)
admin.site.register(Prize)