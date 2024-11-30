from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    playername = models.CharField(max_length=100)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'playername']

    def __str__(self):
        return self.username
    
class Prize(models.Model):
    prize_id = models.CharField(max_length=100)
    prize_name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.prize_id