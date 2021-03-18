from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, role, password=None):
        if not email:
            raise ValueError("Les utilisateurs doivent avoir une adresse mail")
        if not username:
            raise ValueError("Les utilisateurs doivent avoir un username")
        if not first_name:
            raise ValueError("Les utilisateurs doivent avoir un prénom")
        if not last_name:
            raise ValueError("Les utilisateurs doivent avoir un nom")
        if not role:
            raise ValueError("Les utilisateurs doivent avoir un rôle")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, role, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role=role,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=70, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    role = models.CharField(max_length=50)

    # Required
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "role", "username"]

    objects = AccountManager()

    def __str__(self):
        return "[" + self.email + "] - " + self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def has_perms(self, perm, obj=None):
        return self.is_admin
