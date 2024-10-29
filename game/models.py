from django.db import models
from player.models import Player
from machine.models import Machine
from prize.models import Prize
class Game(models.Model):
    game_id = models.CharField(max_length=100)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    prize_id = models.ForeignKey(Prize, on_delete=models.CASCADE)
    play_time = models.DateTimeField()

    def __str__(self):
        return self.game_id