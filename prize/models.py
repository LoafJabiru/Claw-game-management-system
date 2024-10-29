from django.db import models

class Prize(models.Model):
    prize_id = models.CharField(max_length=100)
    prize_name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.prize_id