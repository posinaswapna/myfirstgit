from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mano(request):
    return HttpResponse('we are siblings')