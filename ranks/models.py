from django.db import models

# Create your models here.

class PlayerRank(models.Model):
    rank = models.IntegerField(primary_key=True)
    positionalRank = models.CharField(max_length=100)
    player_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=500)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)

    def __str__(self):
        return str(self.rank) + ' ' + self.full_name
