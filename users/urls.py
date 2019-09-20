from django.urls import path 

from .views import login_user, signup_user

urlpatterns = [
    path('login_user/', login_user, name="login_user"),
    path('signup_user/', signup_user, name="signup_user"),
]