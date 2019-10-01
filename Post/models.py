import os, random

from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


def filename_ext(filepath):
    file_base = os.path.basename(filepath)
    filename, ext = os.path.splitext(file_base)
    return filename, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9498594795)
    name, ext = filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


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
    post_img = models.ImageField(blank=True, null=True, upload_to=upload_image_path)
    # subtitle = models.CharField(max_length=100, null=True)
    published = models.BooleanField(default=1)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    description = RichTextUploadingField()

    def __str__(self):
        return self.title 


"""
class PostCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    bg_image = models.ImageField(upload_to=file_upload)"""