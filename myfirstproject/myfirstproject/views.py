from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello Django Developers This Is Home Page")
    return render(request,'index.html')


def about(request):
    return HttpResponse("Hello Django Developers This Is about Page")

def contact(request):
    return HttpResponse("Hello Django Developers This Is contact Page")