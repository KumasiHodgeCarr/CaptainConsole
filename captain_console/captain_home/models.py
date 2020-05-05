from django.db import models
from games.models import Games, Gamesimage


# Create your models here.
# leikur

class HomeMainImage(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    image = models.ForeignKey(Gamesimage, on_delete=models.CASCADE, default='1')

