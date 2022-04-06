from django.forms import model_to_dict
from django.http import JsonResponse
import json
from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data["id"] = model_data.id
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price
        # yuqoridagi commentga teng kuchli quyida:
        data = model_to_dict(model_data, fields=['id']) # only get id
        data = model_to_dict(model_data) # default -> all fields
    return JsonResponse(data)
    

