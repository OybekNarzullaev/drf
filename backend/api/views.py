from django.forms import model_to_dict
from django.http import JsonResponse
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API view
    """
    if request.method == 'POST':
        return Response(data={"message": "POST not allowed"}, status=405)
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
    return Response(data=data, status=200)
    

