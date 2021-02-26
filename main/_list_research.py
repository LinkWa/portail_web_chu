from urllib import request

from django.http import HttpResponse
from prefect import Flow, task
from django.shortcuts import render

from main.models import FirstFormModel




@task
def list_research(request):
    """template_name = "main/liste_recherche.html"
    a = render(request, template_name, context=None, content_type=None, status=None, using=None)
    return HttpResponse(a)
    liste_recherche(request)"""
    data = FirstFormModel.objects.all()

    context = {
        "datas": data
    }

    if request.method == "POST":
        if "submit_valide" in request.POST:
            temp_model = FirstFormModel.objects.get(id=request.POST.get("submit_valide"))
            temp_model.is_valid = not temp_model.is_valid
            temp_model.save()

    return render(request, "main/liste_recherche.html", context)

with Flow("Liste de recherche") as flow:
    f1 = list_research(request)


flow.register(project_name="list_research")
flow.run()
