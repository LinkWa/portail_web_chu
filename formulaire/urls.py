from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page of our site
    path("formulaire/", views.formulaire, name="formulaire"),
]