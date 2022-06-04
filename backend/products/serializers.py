from rest_framework import serializers
from rest_framework.reverse import reverse
from products.validators import *
from .models import Product
from api.serializers import UserPublicSerializer

class ProductSerializers(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(
        validators=[validate_title, unique_title, validate_no_hello_title]
    )
    my_user_data = serializers.SerializerMethodField(read_only=True)
    owner = UserPublicSerializer(source='user', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    class Meta:
        model = Product
        fields = [
            'my_user_data',
            'owner',
            'email',
            'edit_url',
            'url',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
        ]

    def get_my_user_data(self, obj):
        print(obj)
        return {
            "username": obj.user.username
        }
    
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


