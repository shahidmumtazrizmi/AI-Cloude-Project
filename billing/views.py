from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Invoice, UsageRecord
from django.db import models

@login_required
def usage_summary(request):
    usage = UsageRecord.objects.filter(user=request.user).order_by('-usage_date')
    total_cost = usage.aggregate(total=models.Sum('total_cost'))['total'] or 0
    return render(request, 'billing/usage.html', {'usage': usage, 'total_cost': total_cost})

@login_required
def invoice_list(request):
    invoices = Invoice.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'billing/invoices.html', {'invoices': invoices}) 