from django.shortcuts import render
from .models import *
# Create your views here.

def Index(req):
    return render(req,'index.html')


def Register(request):

    if request.method=='POST':
       
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2 :
            return render(request,'Register.html',{ "msg" : "Password and Confirm Password Does Not Match"})
        else:
            UserModel.objects.create( username = username , password = password1)
            return render(request ,'Login.html')
    return render(request,'Register.html')

def Login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        data = UserModel.objects.filter( username= username , password=password )
        if (data):
            return render(request,'Profile.html')
        else:
            return render(request,'Login.html',{"msg" : "Invalid username or password"})

    return render(request,'Login.html')


def ProfilePage(request):
   
    return render(request,'Profile.html')


def FormPage(request):
    if request.method == 'POST':
        return render(request,'FormPage.html',{ 'msg' : 'Order Confirmed'})
    return render(request,'FormPage.html')