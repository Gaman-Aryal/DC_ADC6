from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('', signupform, name='signup'),
    path('signup1/', signupform1, name='signup1'),
    path('save_owner/', signupowner_save,name='save_owner'),
    path('signup1/save_buyer/', signupbuyer_save,name='save_buyer'),
    path('login/', signinform, name='login'),
    path('login/login/', signinauth),
    path('logout/', logout, name='logout'),

]