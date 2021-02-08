# Our main app urls

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page of our site
    path("recherche/", views.recherche, name="recherche"),
    path("liste_recherche/", views.liste_recherche, name="liste_recherche")
]
