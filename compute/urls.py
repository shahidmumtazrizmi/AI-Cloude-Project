from django.urls import path
from . import views

app_name = 'compute'

urlpatterns = [
    path('', views.instance_list, name='instances'),
    path('create/', views.create_instance, name='create_instance'),
    path('<int:instance_id>/<str:action>/', views.instance_action, name='instance_action'),
]
