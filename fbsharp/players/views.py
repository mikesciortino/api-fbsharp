from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from .serializers import PlayerSerializer
from .filters import PlayerFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Lists all players or creates a new one
# players/
class PlayerList(ListAPIView):

    queryset = (
        Player.objects
        .filter(
            active = True,
        )
        .all()
    )
    serializer_class = PlayerSerializer
    search_fields = ["full_name","team","position", "active"]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PlayerFilter
