from django.db import models
from django.contrib.auth.models import User


class Formulaire(models.Model):
    #nom de l'investigateur responsable
    name_resp = models.CharField(max_length=50)

    # description du projet
    description = models.TextField()
    is_valid = models.BooleanField(default=False)

    # gestionnaire sollicité
    gest_soll = models.CharField(max_length=50)

    # phase1 : initialisation
    proj_name = models.CharField(max_length=50) # projet titre complet
    proj_accronym = models.CharField(max_length=10)
    proj_public_title = models.CharField(max_length=50) # projet titre grand public


    def __str__(self):
        return "Project "+self.proj_name + " with acronym " + self.proj_accronym + " - " + self.description
