from django.urls import path

from .views import (
    login, register, password_reset,
)


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('password_reset/', password_reset, name='password_reset'),
]
