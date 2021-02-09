from django.forms import ModelForm

from main.models import FirstFormModel


# class FirstForm(forms.Form):
#   firstname = forms.CharField(label="Prénom", max_length=50)
#  lastname = forms.CharField(label="Nom", max_length=50)
# description = forms.CharField(label="Description", widget=forms.Textarea)

class FirstForm(ModelForm):
    class Meta:
        model = FirstFormModel
        fields = ["first_name", "last_name", "description"]
        labels = {"first_name": "Prénom", "last_name": "Nom", "description": "Description"}
