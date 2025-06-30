from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail
    post -> create -> New Instance
    put -> Update
    Patch -> Partial Update
    Delete -> Destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    loopup_field = 'pk'
