from django.shortcuts import render
from django.http import HttpResponse

def index (request):

  return HttpResponse("hello world app")

# Create your views here.
