from django.contrib.auth.models import User
from rest_framework import serializers
from ..cart.serializers import CartItemSerializer


class UserSerializer(serializers.ModelSerializer):
    # cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id',
                    'url', 
                    'username', 
                    'email',
                    # 'cart_items', 
                    )
