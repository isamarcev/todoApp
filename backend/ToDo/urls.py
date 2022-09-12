from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', include('tasks.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name="token"),
    path('api-auth/', include('rest_framework.urls')),
]
