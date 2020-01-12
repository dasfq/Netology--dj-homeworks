from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout


def home(request):

    return render(request, 'home.html')


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = User.objects.create_user(username,"",password)
    return render(request, 'registration/signup.html', context={'form': form})

def login(request):
    pass

def logout_user(request):
    logout(request)
    return render(request, 'registration/logout.html', context={})


