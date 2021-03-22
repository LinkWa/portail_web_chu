from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from fobi.models import FormEntry
from formtools.wizard.views import SessionWizardView
# Prefect
from prefect import task

from .forms import *
from .models import Recherche, Comment

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

        f = Recherche(first_name=first_name, last_name=last_name,
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


# -------------------------FOBI---------------------------------------------
def fobi_dashboard(request):
    form_entries = FormEntry._default_manager \
        .filter(user__pk=request.user.pk) \
        .select_related('user')
    context = {"form_entries": form_entries}
    return render(request, "main/fobi_dashboard.html", context)


def delete_fobi_form(request, id_form):
    id_form = int(id_form)
    try:
        selected_form = FormEntry.objects.get(id=id_form)
    except FormEntry.DoesNotExist:
        messages.warning(request, "Ce formulaire n'existe pas")
        return HttpResponseRedirect("/dashboard")
    selected_form.delete()

    messages.success(request, "Formulaire supprimé avec succés !")
    return HttpResponseRedirect("/dashboard")


def create_fobi_form(request):
    return render(request, "main/fobi_create_form.html")


# Formulaires de classification
class ClassificationWizard(SessionWizardView):
    template_name = "main/classification.html"

    def done(self, form_list, **kwargs):
        return render(self.request, 'main/classification.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    @staticmethod
    def get_skip_questions(wizard):
        cleaned_data = wizard.get_cleaned_data_for_step('1') or {}
        if cleaned_data.get("question_2") == "F":
            return {'2': False, '3': False, '4': False, '5': False, '6': False, '7': False,
                    '8': False, '9': False, '10': False, '11': False, '12': False, '13': False,
                    '14': False, '15': False, '16': False}
        else:
            return {}
