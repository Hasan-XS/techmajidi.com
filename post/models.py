from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    title = models.CharField(max_length=60)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # likes = models.ManyToManyRel(User, related_name="likes_posts", blank=True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_details", kwargs={"pk": self.id})
    

class Image(models.Model):
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)
    title_image = models.CharField(max_length=80, blank=True, null=True)
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_image




class Blog(models.Model):
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    title = models.CharField(max_length=60)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_details", kwargs={"pk": self.id})


class ImageBlog(models.Model):
    post = models.ForeignKey(Blog, related_name="images", on_delete=models.CASCADE)
    title_image = models.CharField(max_length=80, blank=True, null=True)
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_image
    
