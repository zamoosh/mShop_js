from .imports import *
from shop.models import Product, Category


def index(request):
    context = {"product": Product.objects.all()}
    return render(request, "shop/index.html", context)
