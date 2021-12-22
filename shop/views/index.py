from .imports import *


def index(request):
    context = {"product": Product.objects.all()}
    return render(request, "shop/index.html", context)
