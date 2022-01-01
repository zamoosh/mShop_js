from django.views.decorators.csrf import csrf_exempt

from .imports import *


@csrf_exempt
def get_date(request):
    response = HttpResponse(request.COOKIES["product"])
    return response
