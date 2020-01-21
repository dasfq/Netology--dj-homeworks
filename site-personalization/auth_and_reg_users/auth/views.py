from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout


def home(request):

    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('1')
        if form.is_valid():
            print('2')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username,"",password)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', context={'form': form})

def login(request):
    pass

def logout_user(request):
    logout(request)
    return render(request, 'registration/logout.html', context={})


