from json import load
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# request handler - function that takes request and returns response
# Create your views here.


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
