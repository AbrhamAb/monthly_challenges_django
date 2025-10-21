from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def january(request):
    return HttpResponse("This is January challenge : Read 5 chapters of a book.")

def february(request):
    return HttpResponse("This is February challenge : Walk for at least 20 minutes every day.")