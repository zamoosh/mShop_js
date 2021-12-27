from .imports import *


def cart(request, p_id):
    selected_product = get_object_or_404(Product, id=request.POST['cart'])
    if "product" in request.COOKIES:
        cookie = request.COOKIES["product"] + "_"
        cookie += selected_product.name
        products = []
        cookies = cookie.split("_")
        for item in cookies:
            products.append(Product.objects.get(name=item))
        context = {
            "products": products
        }
        # order of row 21 and 22 is matter and cookies must set at end...
        response = render(request, "shop/cart.html", context)
        response.set_cookie("product", cookie)
        return response
    else:
        # setting the cookies
        context = {
            "user": request.user,
            "product": selected_product
        }
        response = render(request, "shop/cart.html", context)
        response.set_cookie("product", selected_product)
        return response
