import os,sys

from django.db import models
from django.utils import timezone


def filename_ext(filepath):
    file_base = os.path.basename()
    filename, ext = os.path.splitext(file_base)
    return filename, ext 



CATEGORY_CHOICES = (
    (1, "Biology"),
    (2, "Chemistry"),
    (3, "Physics"),
    (4, "Mathematics")
)

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    category = models.IntegerField(choices=CATEGORY_CHOICES, null=True)
    # subtitle = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title 


"""
class PostCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    bg_image = models.ImageField(upload_to=file_upload)"""