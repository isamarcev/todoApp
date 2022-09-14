from rest_framework import serializers
from .models import Task, SubTask
from django.contrib.auth.models import User





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']




class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['title', 'task']


class TaskSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Task
        fields = '__all__'