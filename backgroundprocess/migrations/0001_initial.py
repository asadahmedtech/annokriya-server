# Generated by Django 2.2.7 on 2019-12-08 07:10

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Select a task to record', max_length=100, verbose_name='Task name')),
                ('history', jsonfield.fields.JSONField(default={}, help_text='JSON containing the tasks history', verbose_name='history')),
            ],
            options={
                'verbose_name': 'Task History',
                'verbose_name_plural': 'Task Histories',
            },
        ),
    ]
