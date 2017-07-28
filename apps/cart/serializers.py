from .models import CartItem
from rest_framework import serializers
from ..products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        # fields = ('id',
        #             # 'url', 
        #             # 'user', 
        #             # 'product',
        #             'user_id',
        #             'product',
        #             'product_details', 
        #             'quantity',
        #             )
        fields = '__all__'
