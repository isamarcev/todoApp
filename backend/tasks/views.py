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
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            queryset = Task.objects.filter(user_id=self.request.user.id).order_by('-id')
        except:
            queryset = []
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
        try:
            queryset = SubTask.objects.all()
        except:
            queryset = []
        return queryset


class TaskSubUserView(APIView):
    permission_classes = []
    def get(self, request, format=None):
        task = Task.objects.filter(user_id=request.user.id)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)


class TaskCreateView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = OnlyTaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDestroyView(generics.DestroyAPIView):
    serializer_class = OnlyTaskSerializer

    def get_queryset(self):
        queryset = Task.objects.get(id=self.request.id)
        return queryset



