from django.db import models
from django.contrib.auth.models import User

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    
class UsageRecord(models.Model):
    RESOURCE_TYPES = [
        ('gpu', 'GPU Compute'),
        ('storage', 'Storage'),
        ('api', 'API Calls'),
        ('bandwidth', 'Bandwidth'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=6, decimal_places=4)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    usage_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)