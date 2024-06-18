from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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
    return render(request,'forgot_password.html')


def change_password(request):
    return render(request, 'change_password.html')


