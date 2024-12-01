# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from .models import Prize, User

def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')  # Replace 'login' with your login url name
  else:
    form = RegisterForm()
  return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Redirect to the desired page after successful login
                return redirect('dashboard')  # Replace 'home' with your desired URL name
            else:
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def welcome_view(request):
   return render(request, 'welcome.html')

def dashboard_view(request):
   session_id = request.session.session_key
   username = request.session.get('username')
   context = {'username': username}
   return render(request, 'dashboard.html', context)

def game1_view(request):
   return render(request, 'index.html')

def prize_view(request):
    records = Prize.objects.all()  # Retrieve all records
    return render(request, 'prizelist.html', {'records': records})