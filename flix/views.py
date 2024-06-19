from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import uuid
from .models import PasswordResetToken
from .sendmail import send_forgot_password_mail
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signUp(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        user=User.objects.create_user(username,email,pass1)
        user.first_name=fname
        user.last_name=lname
        user.save()
        return redirect('login')
    return render(request,'signup.html')

def handleLogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)

            return redirect('home')
        else:
            messages.success(request,'invalid username or password')
            return redirect('login')
    
    return render(request,'login.html')

def forgot_password(request):
    if request.method=='POST':
        username=request.POST.get('username')
        if not User.objects.filter(username=username).exists():
            messages.error(request,'username doesnot exist')
            return redirect('forgot_password')
        else:
            user_obj=User.objects.get(username=username)
            token=str(uuid.uuid4())
            PasswordResetToken.objects.create(user=user_obj,token=token)
            send_forgot_password_mail(user_obj.email,token)
            messages.success(request, "Your password reset link has been sent to email")

    return render(request,'forgot_password.html')


def change_password(request,token):

    return render(request, 'change_password.html')


