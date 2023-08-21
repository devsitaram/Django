from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples =[
        {'name': 'Sitaram Thing', 'age': '23'},
        {'name': 'Gita Thapa', 'age': '20'},
        {'name': 'Aman Gurung', 'age': '18'},
        {'name': 'Jon Marry', 'age': '25'}
    ]
    vagetables =[
        'Pumkin', 'Tomato', 'Potato'
    ]
    return render(request, "home/index.html", context={'page':"Django 2023 Home page",'peoples':peoples, 'vagetables': vagetables,})

def contact(request):
    context = {'page': "Contact"}
    return render(request, "home/contact.html", context)

def about(request):
    context = {'page': "About"}
    return render(request, "home/about.html", context)

def success_page(request):
    return HttpResponse("<h1> This is the django page.</h1>")