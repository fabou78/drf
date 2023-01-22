from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

from api.mixins import StaffEditorPermissionMixin


class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView,
):
    # Combining view is reall comon unless different endpoints are required
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication,
    # ] No longer required because we have condigured default auth in settings

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


# another way to form the url (see products.urls.py)
product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_delete_view = ProductDestroyAPIView.as_view()


# For Class based view we declare functions to handle different cases while
# for function based view we us conditions
# class ProductMixinView(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs):  # HTTP-> get
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):  # HTTP-> get
#         return self.create(request, *args, **kwargs)


# product_mixin_view = ProductMixinView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     '''
#     We are not using this method because we use the combined
#     listcreate view above
#     '''

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# product_list_view = ProductListAPIView.as_view()
