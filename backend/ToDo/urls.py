from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token

from tasks.views import TaskViewSet, TaskApoListView,TaskSubUserView, TaskCreateView, TaskDestroyView

urlpatterns = [
    path('api/', include('tasks.urls')),
    # path('api/logout/', Logout.as_view()),

    path('admin/', admin.site.urls),
    # path('api/tasks', TaskViewSet.as_view({'get': 'list'})),
    # path('api/auth/', include('djoser.urls')),
    path('api/test', TaskApoListView.as_view()),
    path('api/test2/', TaskSubUserView.as_view()),
    path('api/create-task/', TaskCreateView.as_view()),
    path('api/destroy-task/<int:id>', TaskDestroyView.as_view()),

    # path('api/auth/token', obtain_auth_token, name="token"),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('djoser.urls')),
    re_path('api/v1/', include('djoser.urls.authtoken')),

]
