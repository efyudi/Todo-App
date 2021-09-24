from django.urls import path
from .views import RegisterView 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/user_login.html"), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/user_logout.html"), name='user_logout')
]