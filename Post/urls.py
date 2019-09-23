from django.urls import path 

from .views import list_posts, new_post, create_post


urlpatterns = [
    path('list/<int:id>/', list_posts, name="list_posts"),
    path('new/<int:id>/', new_post, name="new_post"),
    path('create/<int:id>/', create_post, name="create_post")
]