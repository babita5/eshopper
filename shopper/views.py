from django.shortcuts import render, redirect
from .views import *
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import *


# Create your views here.
class BaseView(View):
    views={}

class HomeView(BaseView):
    def get(self,request):
        self.views['sliders']=Slider.objects.all()
        self.views['categories']=Category.objects.all()
        self.views['subcategories']=SubCategory.objects.all()
        self.views['ads1']=Ad.objects.filter(rank=1)
        self.views['items']=Item.objects.all()
        self.views['hot_items']=Item.objects.filter(label='hot')
        self.views['new_items']=Item.objects.filter(label='new')
        self.views['sale_items']=Item.objects.filter(label='sale')
        self.views['brands']=Brand.objects.all()

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
        messages.success(request, 'Message is Submitted.')
        return redirect('shopper:contact')
    return render(request, 'contact-us.html')

class ProductDetailView(BaseView):
    def get(self,request,slug):
        category=Item.objects.get(slug=slug).category
        self.views['detail_item']=Item.objects.filter(slug=slug)
        self.views['related_item']=Item.objects.filter(category=category)

        return render(request,'product-details.html',self.views)

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

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.error(request,'Username and Password is incorrect')
            return redirect('shopper:signin')

    return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



