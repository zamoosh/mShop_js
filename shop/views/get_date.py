from .imports import *


@csrf_exempt
def get_date(request):
    response = HttpResponse(request.COOKIES["product"])
    return response
