# Generated by Django 4.1.1 on 2022-09-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_subtask_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='color',
            field=models.CharField(choices=[('blue', '#9fc5f8'), ('green', '#93c47d'), ('orange', '#f9cb9c')], max_length=20, null=True),
        ),
    ]