from django.shortcuts import render
from django.template import RequestContext, Template
from django.http import HttpResponse
from django.db import connection

def index(request):
    response = HttpResponse()
    response.write("<head><title>Default Django Application</title></head>")
    response.write("<h1>Default Django Application<h1>")
    response.write("<h2>It Works!</h2>")
    return response
