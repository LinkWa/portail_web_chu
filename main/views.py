from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import Recherche, Comment

"""
Fonction qui permet d'afficher la page d'accueil

Prend en paramètre un objet django request necessaire au bon fonctionnement du render
"""


def home(request):
    return render(request, "main/home.html")


def recherche(request):
    if request.method == "POST":
        recherche_form = RechercheForm(request.POST)

        if recherche_form.is_valid():
            recherche_instance = recherche_form.instance
            recherche_instance.linked_id_user = request.user.id
            recherche_instance.save()

            return HttpResponseRedirect(
                "/liste_recherche")  # Quand le formulaire est envoyé on redirige vers la page d'acceuil

    else:
        recherche_form = RechercheForm()

    return render(request, "main/recherche.html", {"form": recherche_form})


def liste_recherche(request):
    data = Recherche.objects.all()

    context = {
        "datas": data
    }

    if request.method == "POST":
        if "submit_valide" in request.POST:
            temp_model = Recherche.objects.get(id=request.POST.get("submit_valide"))
            temp_model.is_valid = not temp_model.is_valid
            temp_model.save()

    return render(request, "main/liste_recherche.html", context)


# Modifier la recherche
def update_form(request, first_form_id):
    id_form = int(first_form_id)
    form_instance = Recherche.objects.get(id=id_form)

    if request.method == "POST":
        form = RechercheForm(instance=form_instance, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/liste_recherche")
    else:
        form = RechercheForm(instance=form_instance)
    return render(request, "main/update_form.html", {"form": form})


# Supprimer la recherche
def delete_form(request, first_form_id):  # TODO Supprimer aussi les commentaires associés
    first_form_id = int(first_form_id)
    try:
        selected_first_form = Recherche.objects.get(id=first_form_id)
        comments = Comment.objects.filter(id_recherche=selected_first_form.id)
    except Recherche.DoesNotExist:
        return HttpResponseRedirect("/liste_recherche")
    selected_first_form.delete()
    comments.delete()
    return HttpResponseRedirect("/")


# Vue détaillé de la recherche
def detailed_recherche(request, first_form_id):
    first_form_id = int(first_form_id)

    try:
        selected_first_form = Recherche.objects.get(id=first_form_id)
    except Recherche.DoesNotExist:
        return HttpResponseRedirect("/liste_recherche")

    comments = Comment.objects.filter(id_recherche=first_form_id)

    comment = Comment(id_recherche=first_form_id, username_writer=request.user.username, role_writer=request.user.role)

    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)
        comment_form.save()
        return HttpResponseRedirect("/detailed_form/" + str(first_form_id))
    else:
        comment_form = CommentForm(instance=None)  # TODO Fix le texte qui reste dans la textarea

    context = {
        "data": selected_first_form,
        "comments": comments,
        "comment_form": comment_form
    }
    return render(request, "main/detailed_form.html", context)


# Suppression d'un commentaire
def delete_comment(request, comment_id):
    comment_id = int(comment_id)
    try:
        selected_comment = Comment.objects.get(id=comment_id)
        recherche_id = selected_comment.id_recherche
    except Comment.DoesNotExist:
        return HttpResponseRedirect("/liste_recherche")
    selected_comment.delete()

    return HttpResponseRedirect("/detailed_form/" + str(recherche_id))


# Classification formulaire
def classification(request):
    return render(request, "main/classification.html")
