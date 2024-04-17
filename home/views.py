
from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples = [
        {'name' : 'Rohit ', 'age' : 23},
        {'name' : 'Mohit ', 'age' : 11},
        {'name' : 'Raj ', 'age' : 16},
        {'name' : 'Rahul ', 'age' : 29},
        {'name' : 'Vicky ', 'age' : 12}
    ]

    vegetables = ['potato', 'tomato', 'onion', 'cabbage', 'cauliflower']


    return render(request, 'home/index.html',context={'page' : 'learning Django' ,'peoples': peoples, 'vegetables': vegetables})

def about(request):
    context = {'page' : 'about'}
    return render(request, 'home/about.html', context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "home/contact.html", context)

def success(request):
    return HttpResponse('Success!.')
