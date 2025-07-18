from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from .models import StorageBucket, StorageFile
from .forms import StorageBucketForm, FileUploadForm

COST_PER_GB = 0.10  # Example: $0.10 per GB

@login_required
def bucket_list(request):
    user = request.user
    
    buckets = StorageBucket.objects.filter(user=user).annotate(
        file_count=Count('storagefile')
    ).order_by('-created_at')
    
    # Statistics
    total_storage = buckets.aggregate(total=Sum('size_gb'))['total'] or 0
    bucket_count = buckets.count()
    storage_cost = total_storage * COST_PER_GB

    context = {
        'buckets': buckets,
        'total_storage': total_storage,
        'bucket_count': bucket_count,
        'storage_cost': storage_cost,
    }
    return render(request, 'storage/bucket_list.html', context)

@login_required
def bucket_detail(request, pk):
    bucket = get_object_or_404(StorageBucket, pk=pk, user=request.user)
    
    files = StorageFile.objects.filter(bucket=bucket).order_by('-uploaded_at')
    
    context = {
        'bucket': bucket,
        'files': files,
    }
    return render(request, 'storage/bucket_detail.html', context)

@login_required
def bucket_create(request):
    if request.method == 'POST':
        form = StorageBucketForm(request.POST)
        if form.is_valid():
            bucket = form.save(commit=False)
            bucket.user = request.user
            bucket.save()
            messages.success(request, 'Bucket created successfully.')
            return redirect('bucket_list')
    else:
        form = StorageBucketForm()
    
    return render(request, 'storage/bucket_form.html', {'form': form})

@login_required
def bucket_edit(request, pk):
    bucket = get_object_or_404(StorageBucket, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = StorageBucketForm(request.POST, instance=bucket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bucket updated successfully.')
            return redirect('bucket_list')
    else:
        form = StorageBucketForm(instance=bucket)
    
    return render(request, 'storage/bucket_form.html', {'form': form})

@login_required
def bucket_delete(request, pk):
    bucket = get_object_or_404(StorageBucket, pk=pk, user=request.user)
    
    if request.method == 'POST':
        bucket.delete()
        messages.success(request, 'Bucket deleted successfully.')
        return redirect('bucket_list')
    
    return render(request, 'storage/bucket_confirm_delete.html', {'bucket': bucket})

@login_required
def file_upload(request, bucket_pk):
    bucket = get_object_or_404(StorageBucket, pk=bucket_pk, user=request.user)
    
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.bucket = bucket
            file_instance.save()
            messages.success(request, 'File uploaded successfully.')
            return redirect('bucket_detail', pk=bucket_pk)
    else:
        form = FileUploadForm()
    
    return render(request, 'storage/file_upload.html', {'form': form, 'bucket': bucket})