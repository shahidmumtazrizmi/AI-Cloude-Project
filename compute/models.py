from django.db import models
from django.contrib.auth.models import User

class GPUInstance(models.Model):
    GPU_TYPES = [
        ('H100', 'NVIDIA H100'),
        ('A100', 'NVIDIA A100'),
        ('V100', 'NVIDIA V100'),
        ('RTX4090', 'NVIDIA RTX 4090'),
    ]
    
    STATUS_CHOICES = [
        ('running', 'Running'),
        ('stopped', 'Stopped'),
        ('pending', 'Pending'),
        ('terminated', 'Terminated'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gpu_type = models.CharField(max_length=20, choices=GPU_TYPES)
    gpu_count = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    cpu_cores = models.IntegerField(default=8)
    ram_gb = models.IntegerField(default=32)
    storage_gb = models.IntegerField(default=100)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.gpu_type}"

class ComputeUsage(models.Model):
    instance = models.ForeignKey(GPUInstance, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)