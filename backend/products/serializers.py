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
    # will only work with ModelSerializer and also not need the corresponding
    # get method
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

    def validate_title(self, value):
        queryset = Product.objects.filter(title__exact=value)  # or __iexact
        if queryset.exists():
            raise serializers.ValidationError(
                f'{value} is already a product name'
            )
        return value

    # Another way to create validation would be to create a module
    # i.e. validations.py containing the above function, import it and call it
    # this way =>  title = serializers.CharField(validators=[validate_title])

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
