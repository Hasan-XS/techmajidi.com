from django.urls import path
from .views import (
    posts_view_index,
    post_view_details,
    blogs_view,
    blog_details_view,
    posts_view,
    posts_by_category,
)

urlpatterns = [
    path("", posts_view_index, name="posts_index"),
    path("posts/", posts_view, name="posts"),
    path("post/details/<pk>/", post_view_details, name="post_details"),
    path("post/blogs/", blogs_view, name="blogs"),
    path("post/blogs/details/<pk>/", blog_details_view, name="blog_details"),
    path("post/category/<int:category_id>/", posts_by_category, name="posts_category"),
]
