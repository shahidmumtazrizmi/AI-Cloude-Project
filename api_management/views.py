from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import APIKey, APILog

@login_required
def api_keys(request):
    keys = APIKey.objects.filter(user=request.user)
    return render(request, 'api_management/api_keys.html', {'keys': keys})

@login_required
def api_logs(request):
    logs = APILog.objects.filter(api_key__user=request.user).order_by('-timestamp')[:100]
    return render(request, 'api_management/api_logs.html', {'logs': logs}) 