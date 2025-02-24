from django.urls import path
from . import views
from .views import BlogPostCreateView

urlpatterns = [
    path("", views.blog_index, name="home"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("login/", views.login_page, name="login-page"),
    path("", views.blog_index, name="blog_index"),
    path("blog_post/", views.BlogPostCreateView, name="blog_post"),
]
