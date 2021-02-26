from django.contrib.auth.models import User
from django.db import models


class Recherche(models.Model):
    first_name = models.CharField("Prénom", max_length=50)
    last_name = models.CharField("Nom", max_length=50)

    # description du projet
    description = models.TextField("Description")
    is_valid = models.BooleanField("Validation", default=False)
    linked_id_user = models.PositiveIntegerField(default=0)

    # nom de l'investigateur responsable
    name_resp = models.CharField(max_length=50)

    # gestionnaire sollicité
    CHOICES = [
        ('GEST1', 'CHU Limoges - 2 avenue Martin Luther King, 87042 Limoges Cedex'),
    ]
    gest_soll = models.CharField(
        max_length=5,
        choices=CHOICES,
        default='CHU Limoges - 2 avenue Martin Luther King, 87042 Limoges Cedex',
    )
    # gest_soll = models.ChoiceField('CHU Limoges - 2 avenue Martin Luther King, 87042 Limoges Cedex')

    # phase1 : initialisation
    proj_name = models.CharField(max_length=50)  # projet titre complet
    proj_acronym = models.CharField(max_length=10)
    proj_public_title = models.CharField(max_length=50)  # projet titre grand public

    def __str__(self):
        return self.last_name + " " + self.first_name + " - " + self.description

    def __iter__(self):
        for field in self._meta.fields:
            yield field.verbose_name.title(), field.value_to_string(self)


class Comment(models.Model):
    id_recherche = models.IntegerField()
    username_writer = models.CharField(max_length=30)
    role_writer = models.CharField(max_length=50)
    message = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username_writer + "[" + self.role_writer + "] : " + self.message
