from .models import Cart
from django.contrib.auth.models import User
from rest_framework import viewsets
from serializers import CartSerializer
from rest_framework.decorators import detail_route


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



