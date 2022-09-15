from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, get_object_or_404

from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer, OnlyTaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user_id=self.request.user.id).order_by('-id')
        return queryset

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.delete()
        return Response({'message': 'Todo was success done'})


class SubTaskViewSet(viewsets.ModelViewSet):

    serializer_class = SubTaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(SubTask, id=item)

    def get_queryset(self):
        queryset = SubTask.objects.all()
        return queryset


