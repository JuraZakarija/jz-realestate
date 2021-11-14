from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField()
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields =(
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
        )


class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "username", "phone")
