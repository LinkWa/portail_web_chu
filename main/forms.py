from django import forms


class FirstForm(forms.Form):
    firstname = forms.CharField(label="Prénom", max_length=50)
    lastname = forms.CharField(label="Nom", max_length=50)
    description = forms.CharField(label="Description", widget=forms.Textarea)

