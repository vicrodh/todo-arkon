# Generated by Django 4.0.3 on 2022-04-12 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksession',
            name='final_lenght',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='tasksession',
            name='init_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tasksession',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_session', to='tasks.task'),
        ),
        migrations.AddField(
            model_name='tasksession',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='session_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='tsk_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]