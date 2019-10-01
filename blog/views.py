from django.shortcuts import render 

from users.forms import UserForm


def home_page(request):
    # import pdb; pdb.set_trace()
    template = "index.html"
    form = UserForm()
    context = {"form":form}

    return render(request, template, context)


def contact_page(request):
    template = "contact.html"
    context = {}

    return render(request, template, context)


def about_page(request):
    template = "about.html"
    context = {}

    return render(request, template, context)