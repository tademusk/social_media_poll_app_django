from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")


def tade(request):
    return HttpResponse("and this is custom tade page")


