from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='profile pictures')

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    product_description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="product images", null=True, blank=True)
    post = models.BooleanField(default=False)
    def __str__(self):
        return self.product_name

class Store(models.Model):
    store_name = models.CharField(max_length=200)
    store_description = models.TextField(null=True, blank=True)
    day_created = models.DateTimeField(default=now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stores')
    image = models.ImageField(upload_to="store images")
    product = models.ManyToManyField(Product, related_name='stores')

    def __str__(self):
        return self.store_name
