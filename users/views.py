from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserCreationForm

from .services import post_register_user


def index(request):
    return render(request, 'index.html')


def login(request):
    pass

def register(request):
    form = UserCreationForm(request.POST)  
    post_register_user(request, form)
    if form.is_valid():
        return HttpResponse()
    else:
        print(form.errors)

def password_reset(request):
    pass