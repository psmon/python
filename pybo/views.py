from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("HELLO WORLD PYTHON!!")
# Create your views here.
