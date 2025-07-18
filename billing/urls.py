from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path('usage/', views.usage_summary, name='usage'),
    path('invoices/', views.invoice_list, name='invoices'),
] 