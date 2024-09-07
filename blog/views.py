# Create your views here.
from django.views.generic import DetailView
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from .models import Category, Post, Comment


def blog_index(request):
    context = {"posts": Post.objects.all().order_by("-created_on")}
    return render(request, "blog/home.html", context)


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"title": "login_page"})


# class PostList(View):
#    queryset = Post.objects.filter(status=1)
#    template_name = "index.html"


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "blog/post_detail.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories_name_contains=Category).order_by(
        "-created_on"
    )
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)
