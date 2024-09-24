from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Blog, Post
from clothing.models import Tshirt, Shoes, Pants, Accessory, Hat
from django.views.generic import DetailView

# from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.


# post and index views
def posts_view_index(request):

    posts = Post.objects.all()
    blogs = Blog.objects.all()
    posts_list = list(reversed(posts))[:4]
    blogs_list = list(reversed(blogs))[:4]
    tshirts = list(reversed(Tshirt.objects.all()))[:4]
    context = {
        "posts": posts_list,
        "blogs": blogs_list,
        "tshirts": tshirts,
    }
    return render(request, "posts/index.html", context)


def posts_view(request):

    posts = Post.objects.all()
    posts_list = list(reversed(posts))
    context = {
        "posts": posts_list,
    }
    return render(request, "posts/posts.html", context)


def post_view_details(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(
        request,
        "posts/post-details.html",
        {
            "post": post,
        },
    )


# blog views
def blogs_view(request):
    blogs = list(reversed(Blog.objects.all()))
    return render(
        request,
        "blog/blogs.html",
        {
            "blogs": blogs,
        },
    )


def blog_details_view(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    return render(
        request,
        "blog/blog-details.html",
        {
            "blog": blog,
        },
    )
