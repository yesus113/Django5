from django.http import HttpResponse
from django.shortcuts import render

from core.models import Category,Product


# Create your views here.
def firtView(request):
    data= {
        'firstName': 'John',
        'categories': Category.objects.all()
    }
    return render(request,'index.html', data)

def secondView(request):
    data= {
        'categories': Category.objects.all(),
        'product': Product.objects.all()
    }
    return render(request,'index2.html', data)