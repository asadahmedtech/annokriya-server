# Generated by Django 2.2.7 on 2019-12-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutputTable',
            fields=[
                ('ox1', models.CharField(max_length=255)),
                ('ox2', models.CharField(max_length=255)),
                ('ox3', models.CharField(max_length=255)),
                ('ox4', models.CharField(max_length=255)),
                ('ox5', models.CharField(max_length=255)),
                ('oy1', models.CharField(max_length=255)),
                ('oy2', models.CharField(max_length=255)),
                ('oy3', models.CharField(max_length=255)),
                ('oy4', models.CharField(max_length=255)),
                ('oy5', models.CharField(max_length=255)),
                ('otaskpath', models.ImageField(upload_to=None)),
                ('otaskid', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
    ]