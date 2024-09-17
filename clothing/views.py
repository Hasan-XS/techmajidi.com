from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import *


# Create your views here.


def clothings_view(request):
    shoes = list(reversed(Shoes.objects.all()))[:4]
    tshirt = list(reversed(Tshirt.objects.all()))[:4]
    accessory = list(reversed(Accessory.objects.all()))[:4]
    pants = list(reversed(Pants.objects.all()))[:4]
    hat = list(reversed(Hat.objects.all()))[:4]
    return render(
        request,
        "clothing/clothings.html",
        {
            "tshirts": tshirt,
            "shoes": shoes,
            "accessory": accessory,
            "pants": pants,
            "hat": hat,
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


def tshirt_details_view(request, pk):
    tshirt = get_object_or_404(Tshirt, id=pk)
    return render(
        request,
        "clothing/tshirt/tshirt-details.html",
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


def shoes_details_view(request, pk):
    shoes = get_object_or_404(Shoes, id=pk)
    return render(
        request,
        "clothing/shoes/shoes-details.html",
        {
            "shoes": shoes,
        },
    )


def accessory_view(request):
    accessory = list(reversed(Accessory.objects.all()))
    return render(
        request,
        "clothing/accessory/accessory-details.html",
        {
            "accessory": accessory,
        },
    )


def accessory_details_view(request, pk):
    accessory = get_object_or_404(Accessory, id=pk)
    return render(
        request,
        "clothing/accessory/accessory-details.html",
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


def panst_details_view(request, pk):
    pants = get_object_or_404(Pants, id=pk)
    return render(
        request,
        "clothing/pant/pant-details.html",
        {
            "pant": pants,
        },
    )


def hat_view(request):
    hat = list(reversed(Hat.objects.all()))
    return render(request, "clothing/hat/hat.html", {"hat": hat})


def hat_details_view(request, pk):
    hat = get_object_or_404(Hat, id=pk)
    return render(
        request,
        "clothing/hat/hat-details.html",
        {
            "hat": hat,
        },
    )
