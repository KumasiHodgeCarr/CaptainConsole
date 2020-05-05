from django.db import models


# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()


class Gamesimage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)

class GamesMainimage(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    image = models.ForeignKey(Gamesimage,on_delete=models.CASCADE,default='1')




