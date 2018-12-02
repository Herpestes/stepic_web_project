from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def popular(request, *args, **kwargs):
    return HttpResponse('OK')

def answer(request, *args, **kwargs):
    return HttpResponse('OK')

def ask(request, *args, **kwargs):
    return HttpResponse('OK')

def question(request, *args, **kwargs):
    return HttpResponse('OK')

def signup(request, *args, **kwargs):
    return HttpResponse('OK')

def login(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request, *args, **kwargs):
    return HttpResponse('OK')

