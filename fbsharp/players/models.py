from django.db import models

# Create your models here.

class Player(models.Model):
    player_id = models.CharField(primary_key=True, max_length=500)
    height = models.CharField(max_length=100)
    full_name = models.CharField(max_length=500)
    rotoworld_id = models.CharField(max_length=500)
    weight = models.CharField(max_length=100)
    first_name = models.CharField(max_length=500)
    number = models.IntegerField
    team = models.CharField(max_length=100)
    years_exp = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    news_updated = models.CharField(max_length=500)
    birth_date = models.CharField(max_length=500)
    fantasy_data_id = models.CharField(max_length=500)
    sport = models.CharField(max_length=100)
    rotowire_id = models.CharField(max_length=500)
    college = models.CharField(max_length=500)
    injury_start_date = models.CharField(max_length=500)
    injury_notes = models.CharField(max_length=500)
    yahoo_id = models.CharField(max_length=500)
    high_school = models.CharField(max_length=500)
    age = models.CharField(max_length=500)
    sportradar_id = models.CharField(max_length=500)
    active = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name
