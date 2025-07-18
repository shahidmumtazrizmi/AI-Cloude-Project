from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from .models import DashboardMetrics
from compute.models import GPUInstance
from storage.models import StorageBucket
from billing.models import UsageRecord
from api_management.models import APILog

@login_required
def dashboard_home(request):
    user = request.user
    
    # Get or create dashboard metrics
    metrics, created = DashboardMetrics.objects.get_or_create(
        user=user,
        defaults={
            'gpu_hours_used': 0,
            'storage_used_gb': 0,
            'api_calls_count': 0,
            'monthly_spend': 0
        }
    )
    
    # Aggregate data
    active_gpus = GPUInstance.objects.filter(user=user, status='running').count()
    storage_used = StorageBucket.objects.filter(user=user).aggregate(
        total=Sum('size_gb'))['total'] or 0
    api_calls = APILog.objects.filter(api_key__user=user).count()
    
    # Monthly spend calculation
    monthly_spend = UsageRecord.objects.filter(
        user=user,
        usage_date__month=timezone.now().month
    ).aggregate(total=Sum('total_cost'))['total'] or 0
    
    # Running instances for table
    running_instances = GPUInstance.objects.filter(
        user=user, 
        status='running'
    ).select_related()[:5]
    
    context = {
        'active_gpus': active_gpus,
        'storage_used': f"{storage_used:.1f}",
        'api_calls': f"{api_calls:,}",
        'monthly_spend': f"{monthly_spend:.2f}",
        'running_instances': running_instances,
    }
    
    return render(request, 'dashboard/home.html', context)
