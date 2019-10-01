from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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


def list_posts(request, id):
    template = "posts/list.html"
    posts = Post.objects.filter(category=id, published=True)

    form = UserForm()

    url = request.path
    context = {"posts": posts, "url": url, "form": form, "post_id":id}

    resolve_id(id, context)

    return render(request, template, context)


def detail_post(request, id):
    template = "posts/detail_post.html"
    post = Post.objects.get(pk=id)
    context = {"post": post}
    return render(request, template, context)


def sample_post(request):
    template = "posts/list.html"
    posts = Post.objects.all()#published_date__icontains=timezone.datetime.today.m)

    context = {"posts": posts, "post_id":1}
    
    return render(request, template, context)


@login_required
def new_post(request, id):
    # import pdb; pdb.set_trace()
    template = "posts/new_post.html"
    form = PostForm()
    # import pdb; pdb.set_trace()
    context = {"category": id, "form": form}
    resolve_id(id, context)

    return render(request, template, context)


@login_required
def create_post(request, id, bool):
    if request.method == "POST":
        user = request.user 
        category = id
        request.POST = request.POST.copy()
        request.POST['author'] = user.pk
        request.POST['category'] = category

        if bool == 1:
            request.POST['published'] = True
        else:
            request.POST['published'] = False

        # import pdb; pdb.set_trace()

        form = PostForm(request.POST or None)

        import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            return redirect("list_posts", id=id)
        
        else:
            import pdb; pdb.set_trace()
