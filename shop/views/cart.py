from .imports import *


def cart(request, p_id):
    selected_product = get_object_or_404(Product, id=request.POST['cart'])
    try:
        if request.POST["add to cart"]:
            print("salam")
    except (Exception, TypeError):
        print("na shod!")
        print(p_id)

    return HttpResponse(selected_product)
