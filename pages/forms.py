from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = 'title', 'image', 'description', 'price', 'author', 'author_num', 'condition'

class ProductForm2(forms.ModelForm):
    class Meta:
        model = Electronics
        fields = 'title', 'image', 'description', 'price', 'author', 'author_num', 'condition'

class ProductForm3(forms.ModelForm):
    class Meta:
        model = Furnutures
        fields = 'title', 'image', 'description', 'price', 'author', 'author_num', 'condition'

class ProductForm4(forms.ModelForm):
    class Meta:
        model = Sports
        fields = 'title', 'image', 'description', 'price', 'author', 'author_num', 'condition'

class ProductForm5(forms.ModelForm):
    class Meta:
        model = Households
        fields = 'title', 'image', 'description', 'price', 'author', 'author_num', 'condition'
