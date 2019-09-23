from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=8)
