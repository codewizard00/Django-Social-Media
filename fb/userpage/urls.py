from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
 path("home", views.home, name="home"),
 path("dashboard",views.dashboard,name="dashboard"),
 path("<int:postid>",views.postdel,name="post_del"),
 path("user/<str:username>",views.userprofile,name="userprofile"),
 path("add",views.addpost , name="addpost"),
#  path("user/follow/<str:username>",views.follow,name="follow"),
#  path("search/<str:username>",Search_User.as_view(),name="search_user"),
]
