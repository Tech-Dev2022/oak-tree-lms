from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Oak Learn's first web app")


def contacts(request):
    return HttpResponse("find email below \n chewe.kasonde@outlook.com")