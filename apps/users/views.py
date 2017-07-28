from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from serializers import UserSerializer
from rest_framework.decorators import detail_route, list_route
from ..cart.serializers import CartItemSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



    # @detail_route(methods=['get'])
    # def cartitems(self, request, pk=None):
        
    #     user = self.get_object()
    #     cart_items = user.cartitem_set.all()
    #     serializer = CartSerializer(cart_items, context={'request': request}, many=True)
    #     return Response(serializer.data)

    # @detail_route(methods=['post'])
    # def add_cartitems(self, request, pk=None):
        
    #     user = self.get_object()
    #     cart_items = user.cartitem_set.all()
    #     serializer = CartSerializer(cart_items, context={'request': request}, many=True)
    #     return Response(serializer.data)
