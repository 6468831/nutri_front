from django.shortcuts import render
from django.views import View

from django.template.loader import render_to_string

from .services import get_recipe_list


def get(self, request):
    recipes = get_recipe_list(request)
    return render(request, 'recipes/recipe_list.html')