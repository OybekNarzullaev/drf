from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsStaffEditorPermission
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
    # sessiya authentikatsiyasi
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.IsAdminUser]
    # permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.DjangoModelPermissions] # admin tomonidan qilingan ruxsatlar
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] # custom permission 

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

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()

# barchasini bittada olish uchun: (funcsiyada)
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
        

# barchasini bittada olish class da
class ProductMixinView( 
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin, 
    mixins.RetrieveModelMixin, 
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"

    def get(self, request, *args, **kargs): # http => get
        pk = kargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kargs)
        return self.list(request, *args, **kargs)
    
    def post(self, request, *args, **kargs): # http => post
        return self.create(request, *args, **kargs)
    
    # except from content = None
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content = content)

    def put(self, request, *args, **kwargs): # http -> put
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs): # http -> delete
        return self.destroy(request, *args, **kwargs)
    
product_mixin_view = ProductMixinView.as_view()
