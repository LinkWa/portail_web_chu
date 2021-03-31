# Our main app urls
from django.urls import path

from main.forms import *
from main.views import ClassificationWizard
from . import views

FORM_LIST = [CQuestion1, CQuestion2, CQuestion3, CQuestion4, CQuestion5, CQuestion6, CQuestion7, CQuestion8,
             CQuestion9, CQuestion10, CQuestion11,
             CQuestion12, CQuestion13, CQuestion14, CQuestion15, CQuestion16, CQuestion17, CQuestion18, CQuestion19,
             CQuestion20, CQuestion21]

dict_skip = {"0": ClassificationWizard.get_true_or_false,
             "1": ClassificationWizard.get_true_or_false,
             "2": ClassificationWizard.get_true_or_false,
             "3": ClassificationWizard.get_true_or_false,
             "4": ClassificationWizard.get_true_or_false,
             "5": ClassificationWizard.get_true_or_false,
             "6": ClassificationWizard.get_true_or_false,
             "7": ClassificationWizard.get_true_or_false,
             "8": ClassificationWizard.get_true_or_false,
             "9": ClassificationWizard.get_true_or_false,
             "10": ClassificationWizard.get_true_or_false,
             "11": ClassificationWizard.get_true_or_false,
             "12": ClassificationWizard.get_true_or_false,
             "13": ClassificationWizard.get_true_or_false,
             "14": ClassificationWizard.get_true_or_false,
             "15": ClassificationWizard.get_true_or_false,
             "16": ClassificationWizard.get_true_or_false}

urlpatterns = [
    path("", views.home, name="home"),  # Home page of our site
    path("recherche/", views.recherche, name="recherche"),
    path("liste_recherche/", views.liste_recherche, name="liste_recherche"),
    path("delete_form/<int:first_form_id>", views.delete_form, name="delete_form"),
    path("update_form/<int:first_form_id>", views.update_form, name="update_form"),
    path("detailed_form/<int:first_form_id>", views.detailed_recherche, name="detailed_form"),
    path("delete_comment/<int:comment_id>", views.delete_comment, name="delete_comment"),
    path("classification/",
         ClassificationWizard.as_view(FORM_LIST, condition_dict=dict_skip),
         name="classification"),
]
