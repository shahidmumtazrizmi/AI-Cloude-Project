from django.db import models
from django.contrib.auth.models import User

class DashboardMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gpu_hours_used = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    storage_used_gb = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    api_calls_count = models.IntegerField(default=0)
    monthly_spend = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']