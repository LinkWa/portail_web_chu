# Our main app urls

from django.urls import path

from main.forms import *
from main.views import ClassificationWizard
from . import views

FORM_LIST = [CQuestion1, CQuestion2, CQuestion3, CQuestion4, CQuestion5, CQuestion6, CQuestion7, CQuestion8,
             CQuestion9, CQuestion10, CQuestion11,
             CQuestion12, CQuestion13, CQuestion14, CQuestion15, CQuestion16, CQuestion17, CQuestion18, CQuestion19,
             CQuestion20, CQuestion21]

urlpatterns = [
    path("", views.home, name="home"),  # Home page of our site
    path("recherche/", views.recherche, name="recherche"),
    path("liste_recherche/", views.liste_recherche, name="liste_recherche"),
    path("delete_form/<int:first_form_id>", views.delete_form, name="delete_form"),
    path("update_form/<int:first_form_id>", views.update_form, name="update_form"),
    path("detailed_form/<int:first_form_id>", views.detailed_recherche, name="detailed_form"),
    path("delete_comment/<int:comment_id>", views.delete_comment, name="delete_comment"),
    path("classification/", ClassificationWizard.as_view(FORM_LIST), name="classification"),
    path("dashboard/", views.fobi_dashboard, name="dashboard"),
    path("dashboard/delete/<int:id_form>", views.delete_fobi_form, name="delete_fobi_form")
]
