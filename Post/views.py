from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms.post import PostForm

from users.forms import UserForm


def resolve_id(id, context):
    if id == 1:
        context['biology']=id
        context['login_color']="light text-success"
    elif id == 2:
        context['chemistry']=id
        context['login_color']="primary text-light"
    elif id == 3:
        context['physics']=id
        context['login_color']="dark text-light"
    elif id == 4:
        context['mathematics']=id
        context['login_color']="dark text-light"

# Create your views here.
def list_posts(request, id):
    template = "posts/list.html"
    posts = Post.objects.filter(category=id)

    form = UserForm()

    url = request.path
    context = {"posts": posts, "url": url, "form": form, "post_id":id}

    resolve_id(id, context)

    return render(request, template, context)


@login_required
def new_post(request, id):
    # import pdb; pdb.set_trace()
    template = "posts/new_post.html"
    form = PostForm()
    context = {"category": id, "form": form}
    resolve_id(id, context)

    return render(request, template, context)


@login_required
def create_post(request, id):
    if request.method == "POST":
        user = request.user 
        category = id
        request.POST = request.POST.copy()
        request.POST['author'] = user.pk
        request.POST['category'] = category

        # import pdb; pdb.set_trace()

        form = PostForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect("list_posts", id=id)
        
        else:
            import pdb; pdb.set_trace()
