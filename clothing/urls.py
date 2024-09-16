from django.urls import path
from .views import clothings_view, shoes_view, accessory_view, pants_view, hat_view,tshirt_view

urlpatterns = [
    path("", clothings_view, name="clothings"),
    path("tshirt/", tshirt_view, name="tshirt"),
    path("shoes/", shoes_view, name="shoes"),
    path("accessory/", accessory_view, name="accessory"),
    path("pants/", pants_view, name="pants"),
    path("hat/", hat_view, name="hat"),
]
