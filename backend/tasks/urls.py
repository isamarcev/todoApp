from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import TaskViewSet

urlpatterns = [
    # path('')
]

router = DefaultRouter()
router.register('api/tasks', TaskViewSet, basename='tasks')
urlpatterns += router.urls