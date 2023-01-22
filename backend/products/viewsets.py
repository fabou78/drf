from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list all object (Queryset)
    get -> retrieve Produc Detailed view
    post -> create new instance
    put -> Update
    patch -> Partial update
    delete -> destry/delete the object
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProducGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    '''
    get -> list all object (Queryset)
    get -> retrieve Produc Detailed view
    '''

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
