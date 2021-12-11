from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from userpage.models import *
from django.conf import settings
import uuid
from django.core.mail import send_mail
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
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user=user_obj,auth_token=auth_token)
                profile_obj.save()
                sent_mail_after_registeration(email,auth_token)
                return render(request,"token_sent.html")
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
            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                return redirect("/login")

            profile_obj = Profile.objects.filter(user = user_obj).first()

            user = authenticate(request, username=username, password=password)
            if profile_obj.is_verified:
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




def token_sent(request):
    return render(request,"token_sent.html")

def verify(request,auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            return redirect("/login")
        else:
            return redirect("/error")
    except Exception as e:
        print(e)
        return render(request,"error.html")

def error(request):
    return render(request,"error.html")


def sent_mail_after_registeration(email,token):
    subject = "Your account needs to be verified"
    message =f"hi paste the link to the your account http://127.0.0.1:8000/verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list =[email]
    send_mail(subject,message,email_from,recipient_list)