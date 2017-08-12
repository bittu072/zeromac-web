from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.shortcuts import render

# Create your views here.
def zero_login(request):
    return render(request, "example.html", {})

def zero_register(request):
    return render(request, "example.html", {})

def zero_logout(request):
    return render(request, "example.html", {})
