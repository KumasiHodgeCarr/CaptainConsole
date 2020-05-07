from django.db import models


# Create your models here.


class slides(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=999, blank=True)
