from cProfile import label
from django_filters import rest_framework as filters
from .models import Player

class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class PlayerFilter(filters.FilterSet):
    full_name = CharInFilter(field_name='full_name', label='Player Name')
    team = CharInFilter(field_name='team', label='Team')
    position = CharInFilter(field_name='position', label='Position')
    active = CharInFilter(field_name='active', label='Active')
    
    class Meta:
        model = Player
        #fields = '__all__'
        fields = [str('full_name'), str('team'), str('position'), str('active')]
