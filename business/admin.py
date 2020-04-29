from django.contrib import admin

# Register your models here.
from business.models import Business, Category, Product

admin.site.register(Business)
admin.site.register(Category)
admin.site.register(Product)
