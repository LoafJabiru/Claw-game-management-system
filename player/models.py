from django.db import models

class Player(models.Model):
    player_id = models.CharField(max_length=100)
    player_name = models.CharField(max_length=100)
    balance = models.FloatField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.player_id