from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializers

# Create your views here.
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    