from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def man(request):
    return HttpResponse('<h1>avengers end game<h1>')
