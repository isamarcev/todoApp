from rest_framework import serializers
from .models import Task, SubTask
from django.contrib.auth.models import User





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class TaskSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Task
        fields = '__all__'

class SubTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    class Meta:
        model = SubTask
        fields = '__all__'