from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
    # return HttpResponse('yeah!')

def new_product(request):
    return HttpResponse('<h1>Create a new Product</h1>')

