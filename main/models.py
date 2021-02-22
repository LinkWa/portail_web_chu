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


class Comment(models.Model):
    id_recherche = models.IntegerField()
    username_writer = models.CharField(max_length=30)
    role_writer = models.CharField(max_length=50)
    message = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username_writer + "[" + self.role_writer + "] : " + self.message
