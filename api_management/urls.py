from django.urls import path
from . import views

app_name = 'api_management'

urlpatterns = [
    path('keys/', views.api_keys, name='api_keys'),
    path('logs/', views.api_logs, name='api_logs'),
] 