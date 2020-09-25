from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
import pyrebase

config = {
           'apiKey': "AIzaSyB_dzew07mSNV9xH30nSEoDqqP8XVg5cfo",
    'authDomain': "socialapp-e5a82.firebaseapp.com",
    'databaseURL': "https://socialapp-e5a82.firebaseio.com",
    'projectId': "socialapp-e5a82",
    'storageBucket': "socialapp-e5a82.appspot.com",
    'messagingSenderId': "896171147293",
    'appId': "1:896171147293:web:45e5a476e45272b921c6f4"
  }
 
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
# Create your views here.


def loginUser(request):

    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email)
    print(password)
    try:   
        user = auth.sign_in_with_email_and_password(email,password)
    except:
        print("string")
        messages = "Email or Password Incorrect"
        return render(request,"login.html")
    print(user)
    cont = {'flag' : 'True'}
    return render(request, "index.html", cont)

def register(request):

    fullname=request.POST.get('fullname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email)
    print(password)
    try:
        user=auth.create_user_with_email_and_password(email,password)
        uid = user['localId']
        data={"name":fullname,"status":"1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        print("string")
        message="ACCOUNT REGISTRATION FAILED"
        return render(request,"register.html")
    print(user)    
    return render(request,"login.html")
    

def logoutUser(request):
    logout(request)
    messages.success(request,"You have successfully logged out")
    return redirect("index")

