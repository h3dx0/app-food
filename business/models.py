from django.db import models


# Create your models here.
class Business(models.Model):
    class Meta:
        verbose_name_plural = "Negocios"
        ordering = ['name']

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    status = models.BooleanField(default=True)
    categories = models.ManyToManyField('business.Category', related_name='business')
    logo = models.CharField(max_length=300, blank=True, null=True)
    pickup_time = models.TimeField(default="20:00:00")


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ['name']

    name = models.CharField(max_length=100)


class Product(models.Model):
    class Meta:
        verbose_name_plural = "Productos"
        ordering = ['name']

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.FloatField(default=0.0)


