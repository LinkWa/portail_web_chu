from django.forms import ModelForm

from main.models import Recherche, Comment


class RechercheForm(ModelForm):
    class Meta:
        model = Recherche
        fields = ["gest_soll", "chef_proj", "last_name", "first_name", "proj_name", "proj_acronym", "proj_public_title", "description"]
        labels = {"gest_soll": "Gestionnaire sollicité : ", "chef_proj": "Chef de projet associé", "last_name": "Nom de l'investigateur", "first_name": "Prenom de l'investigateur", "proj_name": "Titre complet du projet", "proj_acronym": "Accronyme du projet", "proj_public_title": "Titre grand public du projet", "description": "Description"}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
        labels = {"message": "Message"}
