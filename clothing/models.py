from django.db import models

# Create your models here.

class Tshirt(models.Model):
    image = models.ImageField(upload_to="tshirt/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title
    


class Shoes(models.Model):
    image = models.ImageField(upload_to="shoes/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title
    

class Accessory(models.Model):
    image = models.ImageField(upload_to="accessory/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title
    

class Pants(models.Model):
    image = models.ImageField(upload_to="pants/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title
    


class Hat(models.Model):
    image = models.ImageField(upload_to="hat/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title