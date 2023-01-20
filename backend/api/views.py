import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest from Django
    # print(dir(request))
    # request.body
    body = request.body  # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except Exception:
        print('trest')

    print(data)
    return JsonResponse(data)
