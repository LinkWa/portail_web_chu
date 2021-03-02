from django.forms import ModelForm
from django import forms
from main.models import Recherche, Comment


class RechercheForm(ModelForm):
    class Meta:
        model = Recherche
        exclude = ["id", "linked_id_user", "is_valid"]
        widgets = {
            'date_but_proj': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'date_publ_proj': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
        labels = {"message": "Message"}
