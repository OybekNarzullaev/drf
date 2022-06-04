from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from products.models import Product

def validate_title(value):
    qs = Product.objects.filter(title__exact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already exists! (from validator)")
    return value

unique_title = UniqueValidator(queryset=Product.objects.all())

def validate_no_hello_title(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"Hello is not allowed")
    return value