from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("datails/<int:p_id>/", views.details, name="detail"),
    path("cart/", views.cart, name="cart"),
    path("show_cart/", views.show_cart, name="show_cart"),
    path("get_date/", views.get_date, name="get_date"),
]
