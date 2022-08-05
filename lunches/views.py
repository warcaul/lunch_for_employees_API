from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from . import serializers
from .models import Menu, Restaurant, Vote
import datetime

class MenuList(generics.ListCreateAPIView):
    """Представлення списку меню. Виводить тільки за цей день"""
    queryset = Menu.objects.filter(day=str(datetime.date.today()))
    serializer_class = serializers.MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def menu_create(self, serializer):
        """додавання меню"""
        serializer.save()




class RestaurantList(generics.ListCreateAPIView):
    """Представлення списку ресторанів"""
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def restaurant_create(self, serializer):
        """Додавання ресторану"""
        serializer.save()




@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def menu_vote(request, pk):
    menu = Menu.objects.get(id=pk)
    user = request.user

    if not post.menu_vote.filter(pk=user.pk).exists():
        post.users_like.add(user)
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_409_CONFLICT)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def menu_unvote(request, pk):
    menu = Menu.objects.get(id=pk)
    user = request.user

    if post.menu_unvote.filter(pk=user.pk).exists():
        post.menu_unvote.remove(user)
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_409_CONFLICT)