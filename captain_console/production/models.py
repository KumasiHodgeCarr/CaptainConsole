from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.

CATEGORY_CHOICES = (
    ('C','Console'),
    ('G','Game')
)

PLATFORM_CHOICES = (
    ('Pl', 'Playstation'),
    ('X', 'Xbox'),
    ('N', 'Nintendo'),
    ('ZA', 'ZX Spectrum'),
    ('S', 'Sega'),
    ('P','PC')
)

class Product(models.Model):
    Product_name        = models.CharField(max_length=255)
    Product_price       = models.FloatField()
    Product_image       = models.CharField(max_length=999, default='bla.jpg')
    Product_description = models.CharField(max_length=999, default='bla')
    Product_category    = models.CharField(choices=CATEGORY_CHOICES,max_length=2,blank=True)
    Product_platform    = models.CharField(choices=PLATFORM_CHOICES,max_length=2)


class Console(models.Model):
    product_id          = models.ForeignKey(Product, on_delete=models.CASCADE)

class Game(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

