from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    message = 'Hello World'
    print(products)
    return render(request, 'home.html', {'products': products, 'message': message})

def about(request):
    return render(request, 'about.html')

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})