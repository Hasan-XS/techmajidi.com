from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.


def clothings_view(request):
    tshirt = Tshirt.objects.all()
    shoes = Shoes.objects.all()
    shoes_list = list(reversed(shoes))[:4]
    tshirt_list = list(reversed(tshirt))[:4]
    return render(
        request,
        "clothing/clothings.html",
        {
            "tshirts": tshirt_list,
            "shoes": shoes_list,
        },
    )


def tshirt_view(request):
    tshirt = list(reversed(Tshirt.objects.all()))
    return render(
        request,
        "clothing/tshirt/tshirts.html",
        {
            "tshirt": tshirt,
        },
    )


def shoes_view(request):
    shoes = list(reversed(Shoes.objects.all()))
    return render(
        request,
        "clothing/shoes/shoes.html",
        {
            "shoes": shoes,
        },
    )


def accessory_view(request):
    accessory = list(reversed(Accessory.objects.all()))
    return render(
        request,
        "clothing/accessory/accessory.html",
        {
            "accessory": accessory,
        },
    )


def pants_view(request):
    pants = list(reversed(Pants.objects.all()))
    return render(
        request,
        "clothing/pant/pants.html",
        {
            "pants": pants,
        },
    )


def hat_view(request):
    hat = list(reversed(Hat.objects.all()))
    return render(request, "clothing/hat/hat.html", {"hat": hat})
