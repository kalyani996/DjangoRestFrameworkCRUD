from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.mixins import (StaffEditorPermissionMixin, UserQueryMixin)

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(
    UserQueryMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def perform_create(self, serializer):
            print(serializer.validated_data)
            # email = serializer.validated_data.pop('email')
            # print(email)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                 content = title
            serializer.save(user=self.request.user, content=content) #form.save() model.save()

    # def get_queryset(self,*args,**kwargs):
    #     qs = super().get_queryset(*args,**kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
        
    #     return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(
    UserQueryMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(
    UserQueryMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    looKup_field = 'pk'
    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    UserQueryMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    loopup_field = 'pk'

    def perform_destroy(self,instance):
       super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
            print(serializer.validated_data)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                 content = "this is cool stufff"
            serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()


#function based view
@api_view(['GET','POST'])
def product_alt_view(request, pk=None,*args, **kwargs):
     method = request.method

     if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        #List view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
     
     if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                 content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invalid":"Not good data"}, status = 400)