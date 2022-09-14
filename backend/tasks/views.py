from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer


class Logout(APIView):

    def get(self, request, format=None):
        print(request.GET)
        print(request.user.auth_token)
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ('title', 'user')
    search_fields = ('title')
    ordering_fields = ('created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_success_headers(self, request):
        print(request)
        super().get_success_headers(self.request)


# class TaskApiList(APIView):
#     def get(self, request):
#         queryset = Task.objects.all()
#         print(queryset)
#         # serializer_class = TaskSerializer(queryset, many=True)
#         return super().get(self, request,)

class TaskApoListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print(request.user)
        return super(TaskApoListView, self).get(self, request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     print(self.request.GET, self.args, self.kwargs, end='\n')
    #     return super().get(self, request, *args, **kwargs)
