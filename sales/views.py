from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import Sale

def home(request):
    return render(request,"sales/home.html ",{})

class SalesList(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SaleDetail(DetailView):
    model = Sale
    template_name = 'sales/detail.html'