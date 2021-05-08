from django.db import models
from django.urls import reverse
STATUS=(('In stock','In Stock'),('Out of stock','Out of Stock'))
LABEL=(('new','New Product'),('hot','Hot Product'),('sale',"Sale product"))
from django.urls import path, include, reverse
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.name


class Slider(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media')
    status = models.CharField(choices=(("active","active"),("","default")),blank = True,max_length=200)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200,unique=True)
    rank=models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    def get_category_url(self):
        return reverse('shopper:category',kwargs= {'slug':self.slug})

class SubCategory(models.Model):
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200, unique=True)
    rank=models.IntegerField(unique=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name=models.CharField(max_length=200)
    rank=models.IntegerField(unique=True)
    image=models.ImageField(upload_to='media')
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    # title=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    rank=models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    def get_brand_url(self):
        return reverse('shopper:brand',kwargs={'rank':self.rank})

class Item(models.Model):
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS)
    label = models.CharField(max_length=60, choices=LABEL, default='new')
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('shopper:product',kwargs={'slug':self.slug})

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    user = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    total = models.IntegerField()

    def __str__(self):
        return self.user

