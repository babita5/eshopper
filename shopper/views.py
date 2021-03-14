from django.shortcuts import render, redirect
from .views import *
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
# Create your views here.
class BaseView(View):
    views={}

class HomeView(BaseView):
    def get(self,request):
        self.views['sliders']=Slider.objects.all()
        self.views['categories']=Category.objects.all()

        return render(request,'index.html',self.views)

class ShopView(BaseView):
    def get(self,request):
        return render(request, 'shop.html')

class ProductView(BaseView):
    def get(self,request):
        return render(request, 'product-details.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject= request.POST['subject']
        message=request.POST['message']

    data=Contact.objects.create(
        name=name,
        email=email,
        subject=subject,
        message=message
    )
    data.save()
    # messages.success(request, 'Message is submitted.')
    return render(request, 'contact-us.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('shopper:signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('shoppper:signup')
            else:
                data=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                data.save()
                messages.success(request, 'Signup Successfully')
                return redirect('shopper:signup')
        else:
            messages.error(request, 'Password Not Matched')
            return redirect('shopper:signup')

    return render(request, 'signup.html')

