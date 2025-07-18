from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum
from .models import GPUInstance, ComputeUsage
from .forms import GPUInstanceForm

@login_required
def instance_list(request):
    user = request.user
    
    instances = GPUInstance.objects.filter(user=user).order_by('-created_at')
    
    # Statistics
    total_instances = instances.count()
    running_count = instances.filter(status='running').count()
    stopped_count = instances.filter(status='stopped').count()
    
    # Monthly compute cost
    monthly_compute_cost = ComputeUsage.objects.filter(
        instance__user=user,
        start_time__month=timezone.now().month
    ).aggregate(total=Sum('cost'))['total'] or 0
    
    context = {
        'instances': instances,
        'total_instances': total_instances,
        'running_count': running_count,
        'stopped_count': stopped_count,
        'monthly_compute_cost': f"{monthly_compute_cost:.2f}",
    }
    
    return render(request, 'compute/instances.html', context)

@login_required
def create_instance(request):
    if request.method == 'POST':
        form = GPUInstanceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            
            # Set hourly rate based on GPU type
            gpu_rates = {
                'H100': 4.50,
                'A100': 3.20,
                'V100': 2.10,
                'RTX4090': 1.80,
            }
            instance.hourly_rate = gpu_rates.get(instance.gpu_type, 2.00)
            instance.save()
            
            messages.success(request, f'Instance {instance.name} created successfully!')
            return redirect('compute:instances')
    else:
        form = GPUInstanceForm()
    
    return render(request, 'compute/create_instance.html', {'form': form})

@login_required
def instance_action(request, instance_id, action):
    instance = get_object_or_404(GPUInstance, id=instance_id, user=request.user)
    
    if action == 'start':
        instance.status = 'running'
        instance.started_at = timezone.now()
        messages.success(request, f'Instance {instance.name} started.')
    elif action == 'stop':
        instance.status = 'stopped'
        messages.success(request, f'Instance {instance.name} stopped.')
    elif action == 'terminate':
        instance.status = 'terminated'
        messages.success(request, f'Instance {instance.name} terminated.')
    
    instance.save()
    return redirect('compute:instances')
