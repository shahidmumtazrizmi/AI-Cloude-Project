from django.urls import path
from . import views

app_name = 'storage'

urlpatterns = [
    path('', views.bucket_list, name='buckets'),
    path('bucket/<int:pk>/', views.bucket_detail, name='bucket_detail'),
    path('bucket/create/', views.bucket_create, name='bucket_create'),
    path('bucket/<int:pk>/edit/', views.bucket_edit, name='bucket_edit'),
    path('bucket/<int:pk>/delete/', views.bucket_delete, name='bucket_delete'),
    path('bucket/<int:bucket_pk>/upload/', views.file_upload, name='file_upload'),
] 