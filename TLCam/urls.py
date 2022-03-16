"""TLCam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from BaseApp import views as baseapp
from Camera import views as camera

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', camera.index, name="home"),
    path('accounts/login/', baseapp.loginPage, name="login"),
    path('accounts/login/validate/', baseapp.validate, name="login_validate"),
    path('accounts/logout/', baseapp.logoutPage, name="logout"),
    path('create/project/', camera.Cam.create_project_page, name="create_project"),
    path('create/project/send/', camera.Cam.create_project, name="create_project_action"),
    path('update/project/<slug:project_slug>/', camera.Cam.update_project, name="update_project"),
    path('update/project/<slug:project_slug>/send/', camera.Cam.update_project_action, name="update_project_action"),
    path('list/projects/', camera.Cam.list_project, name="list_projects"),
    path('start/project/<slug:project_slug>/', camera.Cam.start_project, name="start_project"),
    path('stop/project/<slug:project_slug>/', camera.Cam.stop_project, name="stop_project"),

    path('temp/', camera.temp, name="temp"),
]
