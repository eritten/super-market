from django.shortcuts import render
from .models import Store, Product, Profile
from .forms import CreateStoreForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def home(request):
    return render(request, "home.html")

def create_store(request):
    form = CreateStoreForm()
    if request.method == "POST":
        form = CreateStoreForm(request.POST, request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.owner = request.user
            form.save()

        return render(request, "store.html", {"form": form})
    return render(request, "store.html", {"form": form})

def create_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            password = request.POST.get("password")
            form.password = make_password(password)
            form.save()
            messages.success(request, "account created")
        return render(request, "signup.html", {"form":form})
    return render(request, "signup.html", {"form":form})

def login_user(request):
    if request.method=="POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "dashboard.html")
        messages.error(request, "Login failed")
    return render(request, "login.html")

