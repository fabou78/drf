from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # Below we are renaming the product model's property from get_discount to
    # my_discount
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        return obj.get_discount()
