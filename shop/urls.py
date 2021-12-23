from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:p_id>/", views.details, name="detail"),
    path("cart/<int:p_id>/", views.cart, name="cart"),
]
