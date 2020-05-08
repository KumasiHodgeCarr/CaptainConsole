from django.db import models


# Create your models here.
class Consoles(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    brand = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class ConsolesImage(models.Model):
    image = models.CharField(max_length=999)
    console = models.ForeignKey(Consoles, on_delete=models.CASCADE)

class ConsolesMainImage(models.Model):
    console = models.ForeignKey(Consoles, on_delete=models.CASCADE)
    image = models.ForeignKey(ConsolesImage,on_delete=models.CASCADE,default=1)


class Console_brand_type(models.Model):
    brand = models.CharField(max_length=255)
    image = models.CharField(max_length=999)