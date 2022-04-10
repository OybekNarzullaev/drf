from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]


