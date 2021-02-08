from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from account.forms import RegistrationForm


def register(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            role = form.cleaned_data.get("role")
            raw_password = form.cleaned_data.get("password1")

            account = authenticate(email=email, username=username, first_name=first_name, last_name=last_name,
                                   role=role, password=raw_password)
            login(request, account)
            return redirect("home")

        else:
            context['register_form'] = form

    else:
        form = RegistrationForm()
        context['register_form'] = form

    return render(request, "registers/register.html", context)
