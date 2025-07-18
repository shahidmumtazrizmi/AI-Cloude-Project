from django.urls import path
from . import views

app_name = 'ai_models'

urlpatterns = [
    path('', views.model_list, name='models'),
    path('datasets/', views.dataset_list, name='datasets'),
    path('model/<int:pk>/', views.model_detail, name='model_detail'),
    path('dataset/<int:pk>/', views.dataset_detail, name='dataset_detail'),
] 