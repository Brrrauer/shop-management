from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()
    is_for_sale = models.BooleanField(default=True)
