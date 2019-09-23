from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import SignUpForm, UserForm

# Create your views here.
def signup(request):
    template = "signup.html"
    form = SignUpForm()
    context = {"form": form}
    return render(request, template, context)


def signup_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("home")


def login_(request):
    template = "login.html"
    form = UserForm()
    context = {"form": form}
    return render(request, template, context)


def login_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            next_url = request.POST.get("next")
            user = None
            
            unknown_user = User.objects.filter(email=email)[0]
            if unknown_user is not None:
                user = authenticate(username=unknown_user.username, password=password)
            
            if user is not None:
                login(request, user)
                if next_url is not None:
                    #import pdb; pdb.set_trace()
                    return redirect(next_url)
                else: 
                    return redirect("home")