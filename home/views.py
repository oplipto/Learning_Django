from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render (request, 'home/index.html')

def success(request):
    return HttpResponse('Success!.')
