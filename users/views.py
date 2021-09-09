from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import RegisterForm

# Create your views here.

def register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {'form' : form}
        return render(request, "users/register.html", context)
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print("Form is not valid")
            messages.error(request, "There's an error with your request")
            context = {'form' : form}
            return render(request, "users/register.html", context)
    return render(request, "users/register.html", {})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home/")
            else:
                messages.error(request, f"Invalid Username or Password")
        else:
            messages.error(request, f"Invalid Username or Password")
    form = AuthenticationForm()
    return render(request, "users/login.html", context={"form" : form})

def logout_view(request):
    logout(request)
    return redirect("/")