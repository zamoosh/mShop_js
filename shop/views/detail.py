from .imports import *


def details(request, p_id):
    context = {"product": Product.objects.get(id=p_id)}
    return render(request, "shop/shop/details.html", context)
