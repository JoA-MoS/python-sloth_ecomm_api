from .models import CartItem
from django.contrib.auth.models import User
from rest_framework import viewsets
from serializers import CartSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer


    @list_route
    def user_items(self, request, pk=None):
        user = User.objects.get(pk=pk)
        print user
        cart_items = user.cart_items.all()

        context = {
            'request': request
        }

        post_serializer = CartSerializer(cart_items, many=True, context=context)
        return Response(post_serializer.data)



