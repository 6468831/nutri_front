import requests
from utils.services import get_base_url


def post_register_user(request, form):
    '''send user registration form'''
    print(form)
    URL = get_base_url(request) + 'users/register/'
    r = requests.post(URL, data=form.data).json()
    print(r)