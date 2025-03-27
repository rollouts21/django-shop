from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("service/<slug:slug>/", views.service_detail, name="service_detail"),
]
