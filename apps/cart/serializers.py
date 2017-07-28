from .models import CartItem
from rest_framework import serializers


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = ('url', 
                    'user', 
                    'product',
                    'user_id',
                    'product_id', 
                    'quantity',
                    )
