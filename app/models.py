from django.db import models
from django.urls import reverse
# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    tags = models.TextField(blank=True)  
    img = models.FileField(upload_to="pic/%Y/%m/%d") 

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ('-id',)
    


    def get_absolute_url(self):
        return reverse("details", args=[self.id, self.slug])
    




# products/models.py

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='product_images/')  # Path to save images

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/product/{self.id}/"
    

class Sports_Image_page(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    tags = models.TextField(blank=True)  
    img = models.FileField(upload_to="pic/%Y/%m/%d")# Using ImageField instead of FileField 

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ('-id',)
    
    
    def get_absolute_url(self):
        return reverse("detailss", args=[self.id, self.slug])



# contact_page 

class Contact_page(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    
# slider_page

class image_slider (models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='gallery/')
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


# vector stock 

class vector_page(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    tags = models.TextField(blank=True)  
    img = models.FileField(upload_to="pic/%Y/%m/%d")# Using ImageField instead of FileField 

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ('-id',)
    
    
    def get_absolute_url(self):
        return reverse("vectors", args=[self.id, self.slug])