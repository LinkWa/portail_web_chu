"""portail_web_chu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from registers import views as views_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),  # Check urls in our main app
    path('', include("report.urls")),
    path('', include("django.contrib.auth.urls")),
    path('register/', views_register.register, name="register"),
    # View URLs
    url(r'^fobi/', include('fobi.urls.view')),
    # Edit URLs
    url(r'^fobi/', include('fobi.urls.edit')),
    url(r'^fobi/plugins/form-handlers/db-store/',
        include('fobi.contrib.plugins.form_handlers.db_store.urls')),
]
