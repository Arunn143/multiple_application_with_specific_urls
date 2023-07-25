from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def third(request):
    return render(request,'third.html')


def fourth(request):
    return render(request,'fourth.html')

def string2(request):
    return HttpResponse('This is the string response by app2 project10')

