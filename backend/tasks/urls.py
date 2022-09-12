from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    # path('tasks/', TaskViewSet)
]

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')
urlpatterns += router.urls