from django.shortcuts import render
from profiles.decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def home(request):
    print(request.user.is_authenticated)  # Should print True if the user is logged in
    return render(request, 'home.html')