from django.urls import path

from .services import get_suggestions

urlpatterns = [
    path('get_suggestions/', get_suggestions, name='get_suggestions'),
]