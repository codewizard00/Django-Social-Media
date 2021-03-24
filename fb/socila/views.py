from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

# Create your views here.
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            username= request.POST.get("username")
            email= request.POST.get("email")
            password= request.POST.get("password")
            confpass= request.POST.get("confpass")
            if password==confpass:
                user_obj= User.objects.create_user(username=username,email=email,password=password)
                user_obj.save()
                return render(request,"user_signup.html")
            else:
                return HttpResponse("error")
        else:
            return render(request,"user_signup.html")
    else:
        return redirect("userpage/home")
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("userpage/home")
                
            
            else:
                messages.warning(request, 'Invalid Credentials!')
                return render(request , "user_login.html")
            
        else:
            return render(request , "user_login.html")
    else:
        return redirect("userpage/home")



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request , "user_login.html")
    else:
        return redirect("/login")






