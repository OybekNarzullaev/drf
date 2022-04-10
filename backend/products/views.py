from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from products.models import Product
from products.serializers import ProductSerializers

# # CreateAPIView yangi item qo'shish uchun
# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#     # ruxsatlarni boshqarish uchun
#     def perform_create(self, serializer):
#         title = serializer.validated_data.get("title")
#         content = serializer.validated_data.get("content") or None
#         if content is None:
#             content = title
#         serializer.save(content = content)

# product_create_view = ProductCreateAPIView.as_view()

# bu endi ham yaratish va ham barcha ma'lumotlarni olish uchun
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # ruxsatlarni boshqarish:
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content = content)

product_list_creat_view = ProductListCreateAPIView.as_view()

# RetrieveAPIView bizga get ma'lumotlarini olish uchun yordam beradi:
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

product_detail_view = ProductDetailAPIView.as_view()

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializers(obj, many=False).data
            return Response(data=data)
        queryset = Product.objects.all()
        data = ProductSerializers(queryset, many=True).data
        return Response(data=data)
    if method == "POST":
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            return Response(data={"data": serializer.validated_data}, status=201)
        else:
            return Response(data={"message": "Invalid data"}, status=400)
        

