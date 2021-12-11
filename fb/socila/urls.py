from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_signup , name="user_signup"),
    path("login",views.user_login,name="user_login"),
    path("logout",views.user_logout,name="user_logout"),
    path("token_sent",views.token_sent,name="token_sent"),
    path("verify/<auth_token>",views.verify,name="verify"),
    path("error",views.error,name="error"),
]
    
