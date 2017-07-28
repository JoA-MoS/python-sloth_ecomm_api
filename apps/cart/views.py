from .models import CartItem
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from serializers import CartItemSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


class CartViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


    def list(self, request, user_pk=None):
        queryset = CartItem.objects.filter(user=user_pk)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None):
        queryset = CartItem.objects.filter(pk=pk, user=user_pk)
        cart_item = get_object_or_404(queryset, pk=pk)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)



