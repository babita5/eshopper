"""eshopper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
app_name='shopper'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('shop',ShopView.as_view(),name='shop'),
    path('product',ProductView.as_view(),name='product-details'),
    path('product/<slug>',ProductDetailView.as_view(),name='product'),
    path('contact',contact,name='contact'),
    path('signup', signup,name='signup'),
    path('signin',signin, name='signin'),
    path('logout',logout, name='logout'),

]
