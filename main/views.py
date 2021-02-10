from django.http import HttpResponseRedirect
from django.shortcuts import render
# Prefect
from prefect import Flow, task

from .forms import FirstForm
from .models import FirstFormModel

from django import forms

"""
Cette tache sert a vérifier que les champs du formulaire sont bien remplis de manière logique.
Elle sert aussi à créer un model formulaire qui reprend les informations saisies dans ce dernier.

Elle prend en paramètre un formulaire.
Elle retourne le model prèt à etre envoyé en BDD.
"""


@task()
def verif_form(first_form):
    if first_form.is_valid():
        first_name = first_form.cleaned_data["firstname"]
        last_name = first_form.cleaned_data["lastname"]
        description = first_form.cleaned_data["description"]  # Permet de rendre le formulaire "propre"

        f = FirstFormModel(first_name=first_name, last_name=last_name,
                           description=description)  # Créer le model du formulaire à envoyer en BDD
        return f


"""
Cette tache permet d'envoyer un model formulaire en base de donnée.

Elle prend en paramètre le model à envoyer en bdd
"""


@task()
def save_form(form):
    form.save()  # Sauvegarde le formulaire


"""
Fonction qui permet d'afficher la page d'accueil

Prend en paramètre un objet django request necessaire au bon fonctionnement du render
"""


# Create your views here.
def home(request):
    return render(request, "main/home.html")


"""
Fonction qui permet deux choses, la première est de créer un formulaire vierge.
La deuxième permet de créer un flow de tache qui vérifie et sauvegarde les données entrées dans un formulaire

Prend en paramètre un objet django request qui permet de connaitre l'état d'un formulaire
Renvoie la page du formulaire
"""


def recherche(request):
    if request.method == "POST":  # Si le formulaire est déja créer on rentre là dedans
        first_form = FirstForm(request.POST)  # On récupère les données en POST

        with Flow("Verif and save") as first_flow:  # On créer le flow de sauvegarde du formulaire
            form = verif_form(first_form)
            save_form(form)  # On voit que le flow est composé de deux taches

        first_flow.register(project_name="test")
        first_flow.run()  # On enregistre ce flow et on l'execute

        return HttpResponseRedirect("/")  # Quand le formulaire est envoyé on redirige vers la page d'acceuil
        # TODO Rediriger ailleurs et utilisé les urls django au lieu du chemin relatif

    else:
        first_form = FirstForm()  # On créer un formulaire vide

    return render(request, "main/recherche.html", {"form": first_form})


def liste_recherche(request):
    data = FirstFormModel.objects.all()

    context = {
        "datas": data
    }

    if request.method == "POST":
        if "submit_valide" in request.POST:
            temp_model = FirstFormModel.objects.get(id=request.POST.get("submit_valide"))
            temp_model.is_valid = not temp_model.is_valid
            temp_model.save()

    return render(request, "main/liste_recherche.html", context)

def commentaires(request):
    first_form = FirstForm(request.POST)  # On récupère les données en POST

    if request.method == "POST":
        if "acces_commentaire" in request.POST:
            temp_model = FirstFormModel.objects.get(id=request.POST.get("acces_commentaire"))
            temp_model.save()
            first_form = FirstForm(request.POST)  # On récupère les données en POST

    return render(request, "main/recherche.html", {"form": first_form})

def champCommentaire(first_form):
    commentaire = forms.CharField(label="Commentaire", widget=forms.Textarea)