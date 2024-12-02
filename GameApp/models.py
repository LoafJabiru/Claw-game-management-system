from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    playername = models.CharField(max_length=100)
    balance=models.FloatField(default=0)
    password=models.CharField(max_length=100)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'playername']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.username
    
class Prize(models.Model):
    prize_id = models.CharField(max_length=100)
    prize_name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.prize_id

class PrizeWon(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Foreign key to User model
    prize = models.ForeignKey('Prize', on_delete=models.CASCADE)  # Foreign key to Prize model
    date_won = models.DateTimeField(auto_now_add=True)  # Automatically record date when prize is won

    class Meta:
        unique_together = ('user', 'prize')  # Ensure a user can't win the same prize twice

    def __str__(self):
        return f"{self.user.username} won {self.prize.prize_name} on {self.date_won}"