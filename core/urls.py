from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kandu.urls', namespace='kandu')),
    path('api/', include('kandu_api.urls', namespace='kandu_api')),
]
