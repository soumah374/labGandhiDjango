from django.shortcuts import render

from django.http import HttpResponse


def index():
  return HttpResponse("HELLO WORLD")

# Create your views here.
