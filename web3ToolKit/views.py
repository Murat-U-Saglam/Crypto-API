from json import load
from black import out
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import wallet

# request handler - function that takes request and returns response
# Create your views here.


def index(request):
    myWallet = wallet.objects.all().values()  # get all the data from the database
    output = ""
    for x in myWallet:
        output += x["address"]

    template = loader.get_template("index.html")
    return HttpResponse(output)
