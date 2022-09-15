from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
#
urlpatterns = [
    # path('logout', Logout.as_view())
    # path('tasks/', TaskViewSet.as_view())

]
#
# router = DefaultRouter()
# router.register('tasks', TaskViewSet, basename='tasks')
# urlpatterns += router.urls

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='Tasks')
router.register(r'subtasks', SubTaskViewSet, basename='subtask')

urlpatterns += router.urls

