from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.filter(user_id=1)
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ('title', 'user')
    search_fields = ('title')
    ordering_fields = ('created_at')
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_success_headers(self, request):
        print(request)
        super().get_success_headers(self.request)



class TaskApiView(APIView):
    def get(self, request):
        queryset = Task.objects.all()
        serializer_class = TaskSerializer(queryset, many=True)
        return Response({ 'task': serializer_class.data})