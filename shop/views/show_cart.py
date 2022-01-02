from .imports import *


@csrf_exempt
def show_cart(request):
    product_names = []
    cookies = request.COOKIES["product"]
    cookies = cookies.split("_")
    for item in cookies:
        product_names.append(item)
    product_list = []
    for item in product_names:
        product_list.append(Product.objects.get(id=item))
    context = {
        "products": product_list,
        "user": request.user,
    }
    return render(request, "shop/shop/show_cart.html", context)
