import requests
from utils.services import get_base_url


def get_recipe_list(request):
    PARAMS = {}

    for param in request.GET:
        PARAMS[param] = request.GET.get(param)
    print(PARAMS)
    print(get_base_url(request) + 'recipes/list/')
    URL = get_base_url(request) + 'recipes/list/'
    r = requests.get(URL, params=PARAMS).json()
    return r['recipes']