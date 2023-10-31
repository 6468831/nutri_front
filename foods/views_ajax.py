from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse

from .services import (
    get_food_data,
)
from utils.services import (
    get_suggestions
)

def get_food_data_for_comparison_ajax(request):
    food_slug = request.GET.get('food_slug')
    print('!', food_slug)
    food = get_food_data(request, food_slug)
    result = render_to_string('foods/_nutrients.html', {'food': food})
    return JsonResponse({'result': result})


def food_suggestions_ajax(request):
    model = 'Food'
    app = 'foods'
    name = request.GET.get('name')

    values = get_suggestions(request, 'foods', 'Food', name)
    for value in values:
        value += (reverse('foods:food', kwargs={'food_slug': value[1]}),)
    result = render_to_string('foods/__food_suggestions.html', {'values':values, 'app':app})
    
    return JsonResponse({'result': result})


def compare_food_suggestions_ajax(request):
    model = 'Food'
    app = 'foods'
    name = request.GET.get('name')

    values = get_suggestions(request, 'foods', 'Food', name)

    result = render_to_string('foods/__compare_food_suggestions.html', {'values':values, 'app':app})
    
    return JsonResponse({'result': result})