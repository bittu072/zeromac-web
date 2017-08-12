from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.shortcuts import render
from .forms import UserLoginForm

# Create your views here.
def zero_login(request):
    title = 'Login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return render(request, 'zerousers/example.html', {"form":form, "title":title})

def zero_register(request):
    return render(request, 'zerousers/example.html', {})

def zero_logout(request):
    return render(request, 'zerousers/example.html', {})
