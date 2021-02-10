from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class FirstFormModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name + " " + self.first_name + " - " + self.description

class CommentaireFormModel(models.Models):
    commentaire = models.TextField()