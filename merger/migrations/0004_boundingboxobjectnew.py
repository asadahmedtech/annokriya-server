# Generated by Django 2.2.7 on 2020-01-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merger', '0003_boundingboxobject_taskurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoundingBoxObjectnew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=255)),
                ('y', models.CharField(max_length=255)),
                ('l', models.CharField(max_length=255)),
                ('h', models.CharField(max_length=255)),
                ('taskid', models.CharField(max_length=255)),
                ('taskurl', models.CharField(max_length=2000)),
            ],
        ),
    ]