from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # Below we are renaming the product model's property from get_discount to
    # my_discount
    my_discount = serializers.SerializerMethodField(read_only=True)
    detail_url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    # Below is another example using HyperlinkedIdentityField which
    # will only work with ModelSerializer and also not need the
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'detail_url',
            'edit_url',
            'url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_detail_url(self, obj):
        request = self.context.get('request')  # self.request not usable here
        if request is None:
            return None
        return reverse(
            'product-detail',
            kwargs={'pk': obj.pk},
            request=request,
        )

    def get_edit_url(self, obj):
        request = self.context.get('request')  # self.request not usable here
        if request is None:
            return None
        return reverse(
            'product-edit',
            kwargs={'pk': obj.pk},
            request=request,
        )

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
