from .models import Product, Store, Profile
from django import forms
from django.contrib.auth.models import User

class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['store_name', 'store_description', 'image', ]

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {"password": forms.PasswordInput()}
