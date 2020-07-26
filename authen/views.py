from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import login, logout 


def home(request):
    if request.user.is_authenticated:
            return redirect('/home')                      #not a best way but still!
    return render(request, 'authen/signup.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')                            #not a best way but still!

    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname =request.POST.get('lastname')
        password = request.POST.get('password')
        confirmpassword =request.POST.get('confirmpassword')
        print(username)
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email id already exists")
            else:
                user_ob=User.objects.create_user(first_name= firstname,last_name=lastname,password=password,email=email,username=username)
                user_ob.save()

        else:
            messages.info(request,"password didn't match")

    return redirect('/')

def User_login(request):
    if request.method=='POST':
        user_email = request.POST.get('loginuser','')
        user_password =request.POST.get('loginpassword')

        user = auth.authenticate(username = user_email ,password =user_password) 

        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            return HttpResponse("INVALID USER")    
    else:
        return redirect('/')      

def User_logout(request):
    logout(request)
    return redirect('/')

def check_usrnam(request):
    username = request.GET.get('usrnam', None)
    data = {
        'is_Valid': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)