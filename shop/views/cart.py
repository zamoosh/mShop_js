from .imports import *


def cart(request, p_id):
    selected_product = get_object_or_404(Product, id=p_id)

    return HttpResponse("hello!")
