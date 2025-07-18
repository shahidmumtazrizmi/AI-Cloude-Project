from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AIModel, DataSet

@login_required
def model_list(request):
    models = AIModel.objects.filter(user=request.user).order_by('-created_at')  # type: ignore
    return render(request, 'ai_models/model_list.html', {'models': models})

@login_required
def dataset_list(request):
    datasets = DataSet.objects.filter(user=request.user).order_by('-created_at')  # type: ignore
    return render(request, 'ai_models/dataset_list.html', {'datasets': datasets})

@login_required
def model_detail(request, pk):
    model = get_object_or_404(AIModel, pk=pk, user=request.user)
    return render(request, 'ai_models/model_detail.html', {'model': model})

@login_required
def dataset_detail(request, pk):
    dataset = get_object_or_404(DataSet, pk=pk, user=request.user)
    return render(request, 'ai_models/dataset_detail.html', {'dataset': dataset}) 