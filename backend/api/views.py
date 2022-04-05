from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print("header: ", request.headers)
    data["content_type"] = request.content_type
    data["headers"] = request.headers
    print("this is byte string" ,body)
    print("this is json data" ,data)
    print("data keys: ", data.keys())
    print("GET: ", request.GET)
    print("POST: ", request.POST)
    return JsonResponse({"message": "Hi there this is your Django API Response"})

