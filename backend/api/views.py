from django.http import JsonResponse


def api_home(request, *args, **kargs):
    return JsonResponse({"message": "Hi there this is your Django API Response"})

