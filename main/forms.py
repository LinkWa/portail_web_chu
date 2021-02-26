from django.forms import ModelForm

from main.models import Recherche, Comment


class RechercheForm(ModelForm):
    class Meta:
        model = Recherche
        fields = ["first_name", "last_name", "description"]
        labels = {"first_name": "Prénom", "last_name": "Nom", "description": "Description"}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
        labels = {"message": "Message"}
