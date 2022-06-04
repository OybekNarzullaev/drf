from rest_framework import viewsets
from products.models import Product
from products.serializers import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'

class ProductGenericViewSet(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
