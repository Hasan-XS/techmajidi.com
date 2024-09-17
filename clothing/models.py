from django.db import models
from django.urls import reverse

# Create your models here.


class Tshirt(models.Model):
    image = models.ImageField(upload_to="tshirt/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tshirt_details", kwargs={"pk": self.id})


class Shoes(models.Model):
    image = models.ImageField(upload_to="shoes/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shoes_details", kwargs={"pk": self.id})


class Accessory(models.Model):
    image = models.ImageField(upload_to="accessory/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("accessory_details", kwargs={"pk": self.id})


class Pants(models.Model):
    image = models.ImageField(upload_to="pants/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pant_details", kwargs={"pk": self.id})


class Hat(models.Model):
    image = models.ImageField(upload_to="hat/", null=True, blank=True)
    title = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    caption = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("hat_details", kwargs={"pk": self.id})
