from django.http import HttpResponseRedirect
from django.shortcuts import render
from prefect import Flow, task

from formulaire.models import Formulaire
from formulaire.forms import Formulaire

@task()
def home(request):
    return render(request, "formulaire/index.html")

@task()
def save_form(form):
    form.save()  # Sauvegarde le formulaire

@task()
def verif_form(first_form):
    if first_form.is_valid():
        first_name = first_form.cleaned_data["firstname"]
        last_name = first_form.cleaned_data["lastname"]
        description = first_form.cleaned_data["description"]  # Permet de rendre le formulaire "propre"

        f = Formulaire(first_name=first_name, last_name=last_name,
                           description=description)  # Créer le model du formulaire à envoyer en BDD
        return f

@task()
def formulaire(request):
    if request.method == "POST":  # Si le formulaire est déja créer on rentre là dedans
        first_form = Formulaire(request.POST)  # On récupère les données en POST

        with Flow("Verif and save") as first_flow:  # On créer le flow de sauvegarde du formulaire
            form = verif_form(first_form)
            save_form(form)  # On voit que le flow est composé de deux taches

        first_flow.register(project_name="test")
        first_flow.run()  # On enregistre ce flow et on l'execute

        return HttpResponseRedirect("/")  # Quand le formulaire est envoyé on redirige vers la page d'acceuil

    else:
        first_form = Formulaire()  # On créer un formulaire vide

    return render(request, "main/recherche.html", {"form": first_form})