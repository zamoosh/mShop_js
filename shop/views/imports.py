from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.urls import reverse
from shop.models import *
