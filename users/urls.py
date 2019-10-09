from django.urls import path
from django.contrib.auth.urls import views

from .views import _login, signup, login_user, signup_user, password_reset

urlpatterns = [
    path('login/', _login, name="login"),
    path('login_user/', login_user, name="login_user"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('signup_user/', signup_user, name="signup_user"),
    path('signup/', signup, name="signup"),
    path('password_reset/', password_reset, name="password_reset"),
]