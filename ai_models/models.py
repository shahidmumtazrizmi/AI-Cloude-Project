from django.db import models
from django.contrib.auth.models import User

class AIModel(models.Model):
    MODEL_TYPES = [
        ('classification', 'Image Classification'),
        ('detection', 'Object Detection'),
        ('nlp', 'Natural Language Processing'),
        ('custom', 'Custom Model'),
    ]
    
    STATUS_CHOICES = [
        ('training', 'Training'),
        ('ready', 'Ready'),
        ('failed', 'Failed'),
        ('deploying', 'Deploying'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model_type = models.CharField(max_length=20, choices=MODEL_TYPES)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='training')
    accuracy = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class DataSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file_count = models.IntegerField(default=0)
    total_size_gb = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_labeled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)