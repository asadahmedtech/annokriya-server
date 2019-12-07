# Generated by Django 2.2.7 on 2019-12-06 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskPath',
            fields=[
                ('taskgivenID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('taskPath', models.ImageField(upload_to='post_images')),
                ('taskCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TaskProcessedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.CharField(max_length=255)),
                ('x2', models.CharField(max_length=255)),
                ('x3', models.CharField(max_length=255)),
                ('x4', models.CharField(max_length=255)),
                ('x5', models.CharField(max_length=255)),
                ('y1', models.CharField(max_length=255)),
                ('y2', models.CharField(max_length=255)),
                ('y3', models.CharField(max_length=255)),
                ('y4', models.CharField(max_length=255)),
                ('y5', models.CharField(max_length=255)),
                ('taskpath', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.TaskPath')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
