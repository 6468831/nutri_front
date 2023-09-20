import requests
from utils.services import get_base_url

def get_category_list(request):
    URL = get_base_url(request) + 'foods/categories/'
    r = requests.get(URL).json()
    return r['categories']


def get_current_category(request, category_slug):
    URL = get_base_url(request) + 'foods/current_category/' + category_slug + '/'
    r = requests.get(URL).json()
    return r['current_category']


def get_category_foods(request, category_slug):
    URL = get_base_url(request) + 'foods/category_' + category_slug + '/'
    r = requests.get(URL).json()
    return r['category_foods']


def get_food_list_to_compare(request):
    URL = get_base_url(request) + 'foods/food_list_to_compare/'
    print('!', requests.get(URL))
    r = requests.get(URL).json()
    return r['foods']


def get_food_data(request, food_slug):
    URL = get_base_url(request) + 'foods/' + food_slug + '/'
    r = requests.get(URL).json()
    return r['food_data']


def get_max_nutrient_food_list(request, nutrient_slug):
    URL = get_base_url(request) + 'foods/max_nutrient_' + nutrient_slug + '/'
    r = requests.get(URL).json()
    print(r['foods'])
    return r['foods']


def get_compare_food_facts(request, primary_slug, secondary_slug):
    URL = get_base_url(request) \
        + 'foods/' \
        + primary_slug \
        + '-vs-' \
        + secondary_slug
    r = requests.get(URL).json()
    print(r['compare_food_facts'])
    return r['compare_food_facts']


def get_child_categories(request, category_slug):
    URL = get_base_url(request) + 'foods/get_child_categories/' + category_slug + '/' 
    r = requests.get(URL).json()
    return r['child_categories']
