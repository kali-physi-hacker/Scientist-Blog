from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import SignUpForm, UserForm


# Create your views here.
def signup(request):
    template = "registration/signup.html"
    form = SignUpForm()
    context = {"form": form}
    return render(request, template, context)


def signup_user(request):
    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST['username'] = request.POST.get('email')
        form = SignUpForm(request.POST)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("home")


def _login(request):
    template = "registration/login.html"
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
            
            try:
                unknown_user = User.objects.filter(email=email)[0]
                user = authenticate(username=unknown_user.username, password=password)
            except IndexError:
                messages.error(request, "User is not found")
                return redirect("login")

            if user is not None:
                if user.is_active is not None:
                    # import pdb; pdb.set_trace()
                    login(request, user)
                    if next_url is not None:
                        return redirect(next_url)
                    else:
                        return redirect("home")
                else:
                    messages.error(request, "User Account Disabled. Please Contact The System Administrator")
                    return redirect("login")
            else:
                messages.error(request, "Invalid Password")
                return redirect("login")
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("login")
    else:
        messages.error(request, "Internal server error has occurred, Contact The System Administrator")
        return redirect('home')


def password_reset(request):
    template = "registration/password_reset.html"
    if request.method == "GET":
        context = {}
        return render(request, template, context)