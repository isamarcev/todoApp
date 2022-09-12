from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ('title', 'user')
    search_fields = ('title')
    ordering_fields = ('created_at')