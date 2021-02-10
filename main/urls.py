# Our main app urls

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page of our site
    path("recherche/", views.recherche, name="recherche"),
    path("liste_recherche/", views.liste_recherche, name="liste_recherche"),
    path("delete_form/<int:first_form_id>", views.delete_form, name="delete_form"),
    path("update_form/<int:first_form_id>", views.update_form, name="update_form"),
    path("detailed_form/<int:first_form_id>", views.detailed_recherche, name="detailed_form")
]
