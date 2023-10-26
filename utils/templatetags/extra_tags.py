
from django import template
from utils.services import get_base_domain

register = template.Library()


@register.filter(name='get_domain')
def get_domain(request):
    print('!', request)
    return get_base_domain(request)

@register.filter(name='get_value_from_key')
def get_value_from_key(record, key):
    return record[key]
