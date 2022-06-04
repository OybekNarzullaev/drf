from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'edit_url',
            'url',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'discount'
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse('product-detail', kwargs={"pk":obj.pk}, request=request)
    
    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse('product-edit', kwargs={"pk":obj.pk}, request=request)


