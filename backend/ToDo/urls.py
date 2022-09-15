from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('api/', include('tasks.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('djoser.urls')),
    re_path('api/v1/', include('djoser.urls.authtoken')),

]
