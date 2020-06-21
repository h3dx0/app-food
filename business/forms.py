from django import forms

from business.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('business',)

