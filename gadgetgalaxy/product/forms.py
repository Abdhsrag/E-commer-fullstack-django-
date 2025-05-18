from django import forms
from .models import *
from category.models import Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image', 'sku','category']

class updateProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = forms.IntegerField(required=True)
    image = forms.ImageField(required=False)
    category = forms.ModelChoiceField(queryset=Category.get_all_categories(), required=True)