# Generated by Django 2.2.7 on 2020-01-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0003_auto_20200112_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskpath',
            name='taskTag',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskpathboundingbox',
            name='bb_taskTag',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]