from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maintenance.urls')),  # เชื่อมต่อกับแอป maintenance
]
