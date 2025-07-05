from django import forms
from .models import Item

class ProductForm(forms.ModelForm):
    class Meta:
        model= Item
        fields= '__all__'
        labels= {
            'product_id': 'Product ID',
            'name': 'Product Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier'
        }
        widgets={
            'product_id': forms.NumberInput(
                attrs={'placeholder': 'e.g 1','class':'form-control'}),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g Apple','class':'form-control'}),
            'sku': forms.TextInput(
                attrs={'placeholder': 'e.g SKU123','class':'form-control'}),
            'price': forms.NumberInput(
                attrs={'placeholder':'e.g 10.99','class':'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'placeholder': 'e.g 100','class':'form-control'}),
            'supplier': forms.TextInput(
                attrs={'placeholder': 'e.g Supplier Name','class':'form-control'}),
        }