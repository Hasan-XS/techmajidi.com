from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class PostTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="hasan", password="1234"
        )
        self.post = Post.objects.create(
            title="post title",
            content="post content",
            author = self.user,
        )

    
