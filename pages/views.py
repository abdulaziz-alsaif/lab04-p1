from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
tax_rate = 15

def index(request):
    return render(request, 'pages/index.html')

def test(request):
    return render(request, 'pages/taxrate.html', {'rate': tax_rate})

def calc(request, price):
    price = float(price)
    return HttpResponse(f'Calculted price after tax = {price + (price * tax_rate / 100)}')
