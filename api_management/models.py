from django.db import models
from django.contrib.auth.models import User
import secrets

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_urlsafe(48)
        super().save(*args, **kwargs)

class APILog(models.Model):
    api_key = models.ForeignKey(APIKey, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    response_time_ms = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


    ''' 
    This is the complete foundation for your Django-based AI cloud platform. The structure includes:

1. **Proper Django app organization** with separate modules for each feature
2. **PostgreSQL database models** for all major components
3. **User authentication and role-based access** using Django Allauth
4. **Scalable architecture** ready for AWS deployment
5. **Enterprise-grade structure** similar to Ori.co's platform
    '''