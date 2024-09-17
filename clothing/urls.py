from django.urls import path
from .views import (
    clothings_view,
    shoes_view,
    accessory_view,
    pants_view,
    hat_view,
    tshirt_view,
    tshirt_details_view,
    shoes_details_view,
    accessory_details_view,
    panst_details_view,
    hat_details_view,
)

urlpatterns = [
    path("", clothings_view, name="clothings"),
    path("tshirt/", tshirt_view, name="tshirt"),
    path("tshirt/details/<pk>/", tshirt_details_view, name="tshirt_details"),
    path("shoes/", shoes_view, name="shoes"),
    path("shoes/details/<pk>/", shoes_details_view, name="shoes_details"),
    path("accessory/", accessory_view, name="accessory"),
    path("accessory/details/<pk>/", accessory_details_view, name="accessory_details"),
    path("pants/", pants_view, name="pants"),
    path("pants/details/<pk>/", panst_details_view, name="pant_details"),
    path("hat/", hat_view, name="hat"),
    path("hat/details/<pk>/", hat_details_view, name="hat_details"),
]
