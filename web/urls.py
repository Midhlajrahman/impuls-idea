from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("",views.index,name='index'),
    path("about/",views.about,name="about"),
    path("products/",views.products,name="products"),
    path("service/",views.service,name="service"),
    path("contact/",views.contact,name="contact"),
    path("product_details/<slug:slug>/",views.product_details,name="product_details")
]
