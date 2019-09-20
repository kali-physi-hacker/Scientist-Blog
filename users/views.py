from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login

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


def login_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            next_url = request.POST.get("next")
            user = authenticate(email=email, password=password)
            
            # import pdb; pdb.set_trace()
            if user is not None:
                login(request, user)
                return redirect(next_url)