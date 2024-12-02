from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('index/', views.game1_view, name='game1'),
    path('prizelist/', views.prize_view, name='prizelist'),
    path('deposit/', views.deposit_view, name='deposit'),
    path('index/', views.play_again, name='playagain'),
    path('exchange/', views.redeem_view, name='exchange'),
]