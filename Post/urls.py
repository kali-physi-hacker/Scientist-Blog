from django.urls import path 

from .views import list_posts


urlpatterns = [
    path('list/<int:id>/', list_posts, name="list_posts"),
]