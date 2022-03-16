from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from TLCam.settings import BASE_DIR
from .models import *

# Create your views here.
class Cam:
    def create_project_page(request):
        return render(request, "Camera/create_project.html")


    def create_project(request):
        if request.method == "POST":
            TLProject(
                name = request.POST['name'],
                interval = request.POST['interval'],
                    ).save()
            return render(request, "BaseApp/success.html", {"msg":f"{request.POST['name']} is created successfully"})

        return redirect("create_project")

    def list_project(request):
        projects = TLProject.objects.all()
        return render(request, "Camera/list_projects.html", {"projects":projects})

    def update_project(request, project_slug):
        obj = TLProject.objects.get(slug=project_slug)
        if obj != None:
            return render(request, "Camera/update_project.html", {'obj':obj})
        else:
            raise Http404
    
    def update_project_action(request, project_slug):
        if request.method == "POST":
            obj = TLProject.objects.get(slug=project_slug)
            obj.name = request.POST["name"]
            obj.interval = request.POST["interval"]
            #obj.status = True if request.POST["status"] == "True" else False

            obj.save()
        return redirect("update_project", project_slug)

    def start_project(request, project_slug):
        project = TLProject.objects.get(slug=project_slug)
        if TLProject.objects.filter(status=True).exists():
            prev_project = TLProject.objects.get(status=True)
            prev_project.status = False
            prev_project.save()
        project.status = True
        project.save()

        return redirect('home')

    def stop_project(request, project_slug):
        project = TLProject.objects.get(slug=project_slug)
        project.status = False
        project.save()

        return redirect('home')


@login_required
def index(request):
    print(TLProject)
    return render(request, "Camera/index.html")

def temp(request):
    return HttpResponse(BASE_DIR)
