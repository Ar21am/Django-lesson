from django.shortcuts import render
from .models import Category
from .models import people

# Create your views here.

def home(request):
    mycategories = Category.objects.all()
    context = {
        'mycategories':mycategories
    }
    return render(request, 'home.html', context)

def user(request):
    mypeople = people.objects.all()
    context = {
        'mypeople':mypeople
    }
    return render(request, 'user.html', context)


