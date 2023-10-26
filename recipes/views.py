from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from django.template.loader import render_to_string

from .services import get_recipe_list
from utils.services import is_ajax


class RecipeListView(View):
    def get(self, request):

        recipes = get_recipe_list(request)

        if is_ajax(request):
            recipes_main_block = render_to_string('recipes/recipe_list_main.html', {'recipes': recipes})
            return JsonResponse({'recipes': recipes_main_block})
        else:
            context = {
                'recipes': recipes,
            }
            return render(request, 'recipes/recipe_list.html', context)
