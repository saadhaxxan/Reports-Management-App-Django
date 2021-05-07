from django.urls import path,include
from .views import *
app_name = 'sales'
urlpatterns = [
    path("",home,name="home"),
    path("list/",SalesList.as_view(),name="list"),
    path("detail/<pk>/",SaleDetail.as_view(),name="detail")
]
