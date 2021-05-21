from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
from .utils import *

def home(request):
    form = SalesSearchForm(request.POST or None)
    salesdf = None
    positionsdf = None
    merged_df = None
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if (len(qs))> 0:
            salesdf = pd.DataFrame(qs.values())
            salesdf['customer_id'] = salesdf['customer_id'].apply(get_customer_from_id)
            salesdf['salesman_id'] = salesdf['salesman_id'].apply(get_saleman_from_id)
            salesdf.rename({'customer_id':'customer','salesman_id':'salesman','id':'sales_id'},axis=1,inplace=True)
            salesdf['created'] = salesdf['created'].apply(lambda x:x.strftime("%Y-%m-%d"))
            salesdf['updated'] = salesdf['updated'].apply(lambda x:x.strftime("%Y-%m-%d"))
            position_data = []
            for sale in qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id':pos.id,
                        'product':pos.product.name,
                        'quantity':pos.quantity,
                        'price':pos.price,
                        'sales_id':pos.get_sales_id(),
                    }
                    position_data.append(obj)
            positionsdf = pd.DataFrame(position_data)
            merged_df = pd.merge(salesdf,positionsdf,on='sales_id') 
        else:
            print("No Data")
        salesdf = salesdf.to_html()
        positionsdf = positionsdf.to_html()
        merged_df = merged_df.to_html()
        context = {
        'form':form,
        'salesdf':salesdf,
        'positionsdf':positionsdf,
        'merged_df':merged_df,
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