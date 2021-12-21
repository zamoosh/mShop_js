from .imports import *


def index(request):
    return render(request, "shop/index.html")
