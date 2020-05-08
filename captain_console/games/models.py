from django.db import models


# Create your models here.

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()

    def __str__(self):
        return "{} {} {}".format(self.name,self.description,self.price)


class Gamesimage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)

