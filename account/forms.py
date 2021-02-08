from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Adresse Email valide")
    ROLE_CHOICES = (
        ("investigateur", "investigateur"),
        ("chef_projet", "chef_projet"),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = Account
        fields = ("email", "username", "first_name", "last_name", "role", "password1", "password2")
