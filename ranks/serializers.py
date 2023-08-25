from rest_framework import serializers
from .models import PlayerRank

class PlayerRankSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerRank
        fields = ('rank','full_name', 'team', 'position', 'age', 'priority', 'positionalRank', 'player_id')
        #field = '__all__'
