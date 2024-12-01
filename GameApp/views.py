# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,get_user_model
from .forms import RegisterForm, LoginForm, DepositForm, PlayAgainForm
from .models import Prize, User

User = get_user_model()

def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')  # Replace 'login' with your login url name
  else:
    form = RegisterForm()
  return render(request, 'register.html', {'form': form})

def deposit_view(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit_amount = form.cleaned_data['deposit_amount']
            user = request.user

            # Update user balance
            user.balance += deposit_amount
            user.save()

            # Redirect to dashboard with success message
            return redirect('dashboard')
        else:
            # Handle form validation errors
            return render(request, 'deposit.html', {'form': form})
    else:
        form = DepositForm()
        return render(request, 'deposit.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password,model=User)
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

def play_again(request):
    if request.method == 'POST':
        form = PlayAgainForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            user = User.objects.get(id=user_id)

            if user.balance >= 10:
                user.balance -= 10
                user.save()
                return redirect('game1', success_message='Balance deducted successfully!')
            else:
                return redirect('game1', error_message='Insufficient balance!')
    else:
        return redirect('game1')