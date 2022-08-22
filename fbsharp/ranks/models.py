from django.db import models

# Create your models here.

class PlayerRank(models.Model):
    rank = models.IntegerField(primary_key=True)
    positionalRank = models.CharField(max_length=100)
    player_id = models.CharField(max_length=100)
    full_name = models.CharField(max_length=500)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    adp = models.CharField(max_length=100)
    adpDelta = models.CharField(max_length=100)

    def __str__(self):
        return self.rank + ' ' + self.full_name
