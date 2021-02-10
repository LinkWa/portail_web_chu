from django.forms import ModelForm

from main.models import FirstFormModel
from main.models import CommentaireFormModel

# class FirstForm(forms.Form):
#   firstname = forms.CharField(label="Prénom", max_length=50)
#  lastname = forms.CharField(label="Nom", max_length=50)
# description = forms.CharField(label="Description", widget=forms.Textarea)

class FirstForm(ModelForm):
    class Meta:
        model = FirstFormModel
        fields = ["first_name", "last_name", "description"]
        labels = {"first_name": "Prénom", "last_name": "Nom", "description": "Description"}

#Je sais pas si tu veux qu'on fasse comme ça ou pas ?
class CommentaireForm(ModelForm):
    class Meta:
        model = CommentaireFormModel
        fields = ["commentaire"]
        labels = {"commentaire"}
