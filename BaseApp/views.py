from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginPage(request):
    return render(request, "BaseApp/login.html")

def validate(request):
    user = authenticate(request, 
            username = request.POST['username'], 
            password = request.POST['password'])
    if user is not None:
        login(request, user) 
        return redirect('home')
    else: return render(request, 'BaseApp/login.html', {"msg": "Invalid Credentials"})

def logoutPage(request):
    logout(request)
    return redirect("home")
