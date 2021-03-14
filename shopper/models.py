from django.db import models

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

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200,unique=True)
    # subcategory_name=models.CharField(max_length=200, blank=True, default)
    # subcategory_slug=models.CharField(max_length=200, unique=True, default)

    def __str__(self):
        return self.name