from cProfile import label
from django_filters import rest_framework as filters
from .models import PlayerRank

class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class PlayerRankFilter(filters.FilterSet):
    full_name = CharInFilter(field_name='full_name', label='Player Name')
    team = CharInFilter(field_name='team', label='Team')
    position = CharInFilter(field_name='position', label='Position')
    
    class Meta:
        model = PlayerRank
        #fields = '__all__'
        fields = [str('full_name'), str('team'), str('position')]
