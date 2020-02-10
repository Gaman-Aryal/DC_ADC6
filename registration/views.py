from django.shortcuts import render
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError



# Create your views here.
from registration.models import Buyer, Owner


def signupform(request):
    return render(request, 'ownerregistration.html')

def signupform1(request):
    return render(request, 'buyerregistration.html')

def signupowner_save(request):
    if request.method == "GET":
        return render(request, 'ownerregistration.html')
    else:
        try:
            user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['first_name'],
                                            last_name=request.POST['last_name'],
                                            email=request.POST['email'], password=request.POST['password'])
            user.save()
            own = Owner(First_Name=request.POST['first_name'],
                        Last_Name=request.POST['last_name'],
                        Username=request.POST['username'],
                        Password=request.POST['password'],
                        Gender=request.POST['gender'],
                        Phone_number=request.POST['phone_number'],
                        E_mail=request.POST['email'])
            own.save()
            messages.info(request, "Successfully Created.You can Sign In.")
            return redirect('login')

        except IntegrityError:
            messages.error(request, "Username Already Exists.Please Try again Another One.")
            return redirect('signup')

def signupbuyer_save(request):
    if request.method == "GET":
        return render(request, 'buyerregistration.html')
    else:
        try:
            user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['first_name'],
                                            last_name=request.POST['last_name'],
                                            email=request.POST['email'], password=request.POST['password'])
            user.save()
            buy = Buyer(First_Name=request.POST['first_name'],
                        Last_Name=request.POST['last_name'],
                        Username=request.POST['username'],
                        Password=request.POST['password'],
                        Gender=request.POST['gender'],
                        Phone_number=request.POST['phone_number'],
                        E_mail=request.POST['email'])

            buy.save()
            messages.info(request, "Successfully Created.You can Sign In.")
            return redirect('login')

        except IntegrityError:
            messages.error(request, "Username Already Exists.Please Try again Another One.")
            return redirect('signup')


def signinform(request):
    return render(request, 'login.html')


def signinauth(request):
    if request.method == "GET":
        return render(request, 'login.html')

    else:
        auth_user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(auth_user)
        if auth_user is not None:
            login(request, auth_user)
            return redirect('/')

        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')


