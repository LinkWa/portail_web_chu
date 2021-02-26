# Report urls

from django.urls import path
from . import views

urlpatterns = [
    path("report/<int:recherche_id>", views.create_report, name="create_report")
]
