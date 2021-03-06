from .imports import *


@csrf_exempt
def cart(request):
    selected_product = get_object_or_404(Product, id=request.POST['cart'])
    cookie = ""
    if "product" in request.COOKIES:
        cookie += request.COOKIES["product"] + "_"
    cookie += str(selected_product.id)
    # setting the cookies
    response = redirect("shop:show_cart")
    response.set_cookie("product", cookie)
    try:
        print(request.POST['cart'])
    except (Exception, TypeError):
        print("kir shodi!")
    return response
