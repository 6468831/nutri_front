


def get_base_url(request):
    return request.scheme + '://' + request.get_host().split(':')[0] + ':8000/api/v1/'

def get_base_domain(request):
    print(type(request))
    print(request)
    return request.scheme + '://' + request.get_host().split(':')[0] + ':8000'


def is_ajax(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'
