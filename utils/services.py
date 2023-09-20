


def get_base_url(request):
    return request.scheme + '://' + request.get_host().split(':')[0] + ':8000/api/v1/'