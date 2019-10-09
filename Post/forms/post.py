from django import forms 
from Post.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post 
        fields = ["title", "description", "author", "category", "post_img", "published"]


