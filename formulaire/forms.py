from django import forms


class Formulaire(forms.Form):
    # nom de l'investigateur responsable
    name_resp = forms.CharField(label="Nom", max_length=50)

    # description du projet
    description = forms.CharField(label="Description", widget=forms.Textarea)

    # gestionnaire sollicité
    gest_soll = forms.CharField(label="Gestionnaire sollicité", max_length=50)

    # phase1 : initialisation
    proj_name = forms.CharField(label="titre complet du projet", max_length=50)  # projet titre complet
    proj_accronym = forms.CharField(label="accronyme du projet", max_length=10)
    proj_public_title = forms.CharField(label="titre grand public du projet", max_length=50)  # projet titre grand public