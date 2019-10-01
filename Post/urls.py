from django.urls import path 

from .views import list_posts, new_post, create_post, detail_post


urlpatterns = [
    path('list/<int:id>/', list_posts, name="list_posts"),
    path('detail/<int:id>/', detail_post, name="detail_post"),
    path('new/<int:id>/', new_post, name="new_post"),
    path('create/<int:id>/<int:bool>/', create_post, name="create_post")
]