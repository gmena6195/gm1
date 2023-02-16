from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import*

def home(request):

    return render(request,'accounts/dashboard.html')

def products(request):
    query_results = tag.objects.all()
    query_results2 = occasion.objects.all()


    context = {'tag':query_results, 'occasion': query_results2}
    return render(request,'accounts/products.html', context)



def customer(request):
    return render(request,'accounts/customer.html')


