from django.db import models
from django.conf import settings

def get_next_id():
    try:
        next_id = int(Task.objects.order_by('-id').first().id) + 1
    except AttributeError:
        next_id=1
    print(next_id)
    return next_id

class Task(models.Model):
    id = models.IntegerField(unique=True, default=get_next_id, primary_key=True)
    title = models.CharField(max_length=200)
    color_list = [('blue', '#9fc5f8'), ('green', '#93c47d'), ('orange', '#f9cb9c')]
    color = models.CharField(max_length=20, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.title}'


class SubTask(models.Model):
    title = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)