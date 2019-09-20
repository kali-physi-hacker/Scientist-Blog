from django.shortcuts import render 

from users.forms import UserForm


def home_page(request):
    template = "index.html"
    form = UserForm()
    context = {"form":form}
    return render(request, template, context)