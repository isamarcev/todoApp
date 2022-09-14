from rest_framework import serializers
from .models import Task, SubTask
from django.contrib.auth.models import User





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email',]



class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['title', 'task', 'id']


class OnlyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'color',]


class TaskSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    sub = SubTaskSerializer(many=True, source='subtask_set.all', read_only=True)
    class Meta:
        model = Task
        fields = ['title', 'color', 'sub', 'id']