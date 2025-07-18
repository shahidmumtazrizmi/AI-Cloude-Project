from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('dashboard.urls')),
    path('compute/', include('compute.urls')),
    path('storage/', include('storage.urls')),
    path('ai-models/', include('ai_models.urls')),
    path('billing/', include('billing.urls')),
    path('api/', include('api_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
cloudai_platform/
├── manage.py
├── requirements.txt
├── cloudai_platform/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts/
├── dashboard/
├── compute/
├── storage/
├── ai_models/
├── billing/
├── api_management/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── templates/
    ├── base.html
    ├── dashboard/
    ├── compute/
    ├── storage/
    └── partials/
'''