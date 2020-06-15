from django.db import models

ORDER_STATUS = (
    ('NEW', 'Nueva'),
    ('COMPLETED', 'Completada'),
    ('CANCELLED', 'Cancelada')
)
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

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ['name']

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name_plural = "Paquete"
        ordering = ['name']

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.FloatField(default=0.0, help_text="Este es el precio original sin descuento")
    discount = models.IntegerField(default=50, help_text="Este valor hace referencia en porciente")
    business = models.ForeignKey('business.Business', on_delete=models.PROTECT, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.CharField(default=000, max_length=12)
    units = models.IntegerField(default=1)
    created = models.DateTimeField(auto_created=True)
    total = models.FloatField(default=0.0)
    status = models.CharField(choices=ORDER_STATUS, default='NEW', max_length=12)


class OrderProduct(models.Model):
    order = models.ForeignKey('business.Order', related_name='products', on_delete=models.CASCADE)
    product = models.ForeignKey('business.Product', related_name='order', on_delete=models.CASCADE)
    units = models.IntegerField(default=1)
    total = models.FloatField(default=0.0)
