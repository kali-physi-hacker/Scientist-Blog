from django.urls import path 

from .views import list_posts, new_post, create_post, detail_post, edit_post, update_post


urlpatterns = [
    path('list/<int:id>/', list_posts, name="list_posts"),
    path('detail/<int:id>/', detail_post, name="detail_post"),
    path('new/<int:id>/', new_post, name="new_post"),
    path('create/<int:_id>/<int:_bool>/', create_post, name="create_post"),
    path('edit/<int:_id>/', edit_post, name="edit_post"),
    path('update/<int:_id>/', update_post, name="update_post")
]