from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.WelcomePage, ),
    path('main/signup/', views.Signup, name='SignUp'),
    path('main/login/', views.Login, name="Login"),
    path('main/usersignin/', views.handle_signup, name='handle_usersign'),
    path('main/userlogin/', views.handle_login, name='handle_logins'),
    
    path('Admin/', include('Admin_app.urls')),
]