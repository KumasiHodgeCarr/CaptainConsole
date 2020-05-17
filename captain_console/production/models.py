from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django_countries.fields import CountryField

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
    slug                = models.SlugField()

    def __str__(self):
        return self.Product_name

    def get_absolute_url(self):
        return reverse("production:product", kwargs= {
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("production:add-to-cart", kwargs= {
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("production:remove-from-cart", kwargs= {
            'slug': self.slug
        })
class Console(models.Model):
    product_id          = models.ForeignKey(Product, on_delete=models.CASCADE)

class Game(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.Product_name}'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

class BillingAddress(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    countries = CountryField(multiple=True)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
