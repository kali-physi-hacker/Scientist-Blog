from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models.fields.files import FileField, ImageFieldFile
from django.utils import timezone

from Post.models import Post

user = User.objects.create(username='test_user', email="test@email.com", password="password")
title = "Testing Title"
category = 0
post_img = ImageFieldFile(instance=None, field=FileField(), name="products/1397908421/1397908421.jpg")
published = True
published_date = timezone.now()
created_date = timezone.now()
description = "Just a description for testing Kali Scientist Blog Model"


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(author=user, title=title, category=category,
                            post_img=post_img, published=published,
                            published_date=published_date, created_date=created_date,
                            description=description)

    def test_author_field_title(self):
        post = Post.objects.get(id=1)
        field_title = post._meta.get_field('title').verbose_name
        self.assertEquals(field_title, 'title')

    def test_author_field_user(self):
        post = Post.objects.get(id=1)
        field_user = post._meta.get_field('author').verbose_name
        self.assertEquals(field_user, 'author')
