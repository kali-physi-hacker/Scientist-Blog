from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import datetime

from .models import Post
from .forms.post import PostForm

from users.forms import UserForm


def datetimes_of_week():
    today_date = datetime.datetime.today()
    start = today_date - datetime.timedelta(today_date.weekday())
    end = start + datetime.timedelta(days=6)
    return start, end


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
    week_day_start, week_day_end = datetimes_of_week()
    posts = Post.objects.filter(published_date__gte=week_day_start).filter(published_date__lte=week_day_end)

    context = {"posts": posts, "post_id": 1, "sample_posts": True}
    
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
def create_post(request, _id, _bool):
    if request.method == "POST":
        user = request.user 
        category = _id
        request.POST = request.POST.copy()
        request.POST['author'] = user.pk
        request.POST['category'] = category

        if _bool == 1:
            request.POST['published'] = True
        elif _bool == 0:
            request.POST['published'] = False

        form = PostForm(request.POST or None)
        # import pdb; pdb.set_trace()

        if form.is_valid():
            form.save()
            return redirect("list_posts", id=_id)


@login_required
def edit_post(request, _id):
    post = Post.objects.get(pk=_id)
    if request.user == post.author:
        template = "posts/edit_post.html"
    else:
        template = "posts/unauthorized.html"
    form = PostForm()
    context = {"form": form, "post": post}
    return render(request, template, context)


@login_required
def update_post(request, _id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=_id)
        request.POST = request.POST.copy()
        request.POST['author'] = post.author.pk
        request.POST['category'] = post.category
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post Update Successfully!")
            return redirect('detail_post', id=_id)
        else:
            import pdb; pdb.set_trace()
            messages.error(request, "There's an error with the submitted data. Please Try Again")
            return redirect('edit_post', id=_id)
