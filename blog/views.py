# Create your views here.
from django.views.generic import DetailView, CreateView
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404

from blog.forms import PostForm
from blog.forms import CommentForm
from .models import Category, Post, Comment
from django.http import HttpResponseRedirect


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
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/about.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name=category).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def BlogPostCreateView(CreateView):
    model = Post
    template_name = "post.html"
    fields = "__all__"


#
# def blog_post(request):
#     post_form = PostForm()
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = Post(
#                 title=form.cleaned_data["title"],
#                 author=form.cleaned_data["author"],
#                 body=form.cleaned_data["body"],
#             )
#             post.save()
#
#     context = {
#         "post_form": post_form,
#     }
#     args = {}
#     args["post_form"] = post_form
#
#     return render(request, "blog_post.html", args)
