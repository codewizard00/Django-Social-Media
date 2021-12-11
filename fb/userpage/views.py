from django.shortcuts import render,redirect,HttpResponse
from .models import *
import json
from django.views.generic import ListView
from django.contrib.auth.models import User
# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        profile = Userprofile.objects.get(user=request.user)
        posts = Post.objects.filter(user=request.user).order_by("-pk")
        return render(request, "dashboard.html",{"posts":posts,"profile":profile} ) 
    else:
        return redirect("/login")


def home(request):
    if request.user.is_authenticated:
        posts=Post.objects.all().order_by("-pk")
        return render(request , "home.html",{"posts":posts})
    else:
        return redirect("/login")

def userprofile(request,username):
    user = User.objects.filter(username=username)
    profile = Userprofile.objects.get(user=user[0])
    posts = Post.objects.filter(user=user[0])
    data = {"profile":profile,"posts":posts}
    return render(request, "userprofile.html",data)

def postdel(request, postid ):
    post_ =Post.objects.filter(pk=postid)
    image_path=post_[0].image.url
    post_.delete()
    return redirect("/userpage/dashboard")


def addpost(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title","")
        desc = request.POST.get("desc","")
        image= request.FILES["image"]
        post_obj = Post(user=user,title=title,desc=desc,image=image)
        post_obj.save()
        return redirect("/userpage/home")
    else :
        return HttpResponse("hello")
        

