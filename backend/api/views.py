import json
from django.forms import model_to_dict
from products.models import Product
from products.serializers import ProductSerializers

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
        # data = model_to_dict(model_data, fields=['title','sale_price']) # only gets id and sale price
        # data = model_to_dict(model_data) # default -> all fields

        data = ProductSerializers(instance=model_data).data
    return Response(data=data, status=200)
    

@api_view(['POST'])
def post_data(request, *args, **kargs):
    # validation
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(status=400, data={"message": "Bad Request"})