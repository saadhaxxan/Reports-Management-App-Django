from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd

def home(request):
    form = SalesSearchForm(request.POST or None)
    salesdf = None
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if (len(qs))> 0:
            salesdf = pd.DataFrame(qs.values()).to_html()
        else:
            print("No Data")
        context = {
        'form':form,
        'salesdf':salesdf,
        }
        return render(request,"sales/home.html ",context)
    context = {
        'form':form
    }
    return render(request,"sales/home.html ",context)

class SalesList(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SaleDetail(DetailView):
    model = Sale
    template_name = 'sales/detail.html'