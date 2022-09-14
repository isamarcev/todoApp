from django.core.management import BaseCommand

from ...models import SubTask, Task


class Command(BaseCommand):

    def handle(self, *args, **options):
        tasks = Task.objects.all()
        for task in tasks:
            subtask = SubTask.objects.bulk_create([SubTask(title=task.title, task=task),
                                                   SubTask(title='Tasks2', task=task),])