from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import PlayerRank
from .serializers import PlayerRankSerializer
from .filters import PlayerRankFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Lists all players or creates a new one
# players/
class RanksList(ListAPIView):

    queryset=PlayerRank.objects.all()
    serializer_class = PlayerRankSerializer
    search_fields = ["full_name","team","position"]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PlayerRankFilter
