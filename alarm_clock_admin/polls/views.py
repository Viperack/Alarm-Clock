from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    time = datetime.datetime.now()
    html = "<html><body><h1>Rendered at %s</h1></body></html>" % time

    return HttpResponse(html)