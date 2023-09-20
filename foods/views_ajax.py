from django.http import JsonResponse
from django.template.loader import render_to_string


from .services import (
    get_food_data,
)


def get_food_data_for_comparison_ajax(request):
    food_slug = request.GET.get('food_slug')
    print('!', food_slug)
    food = get_food_data(request, food_slug)
    result = render_to_string('foods/_nutrients.html', {'food': food})
    return JsonResponse({'result': result})