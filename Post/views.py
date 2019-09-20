from django.shortcuts import render
from .models import Post

from users.forms import UserForm

# Create your views here.
def list_posts(request, id):
    template = "posts/list.html"
    posts = Post.objects.filter(category=id)

    form = UserForm()

    url = request.path
    context = {"posts": posts, "url": url, "form": form}

    if id == 1:
        context['biology']=id
    elif id == 2:
        context['chemistry']=id
    elif id == 3:
        context['physics']=id
    elif id == 4:
        context['mathematics']=id

    return render(request, template, context)