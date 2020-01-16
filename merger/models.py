from django.db import models
from distributor.models import TaskPath, TaskPathBoundingBox
# Create your models here.

class OutputTable(models.Model):
    ox1=models.CharField(max_length=255)
    ox2=models.CharField(max_length=255)
    ox3=models.CharField(max_length=255)
    ox4=models.CharField(max_length=255)
    ox5=models.CharField(max_length=255)

    oy1=models.CharField(max_length=255)
    oy2=models.CharField(max_length=255)
    oy3=models.CharField(max_length=255)
    oy4=models.CharField(max_length=255)
    oy5=models.CharField(max_length=255)
    otaskpath=models.ImageField(upload_to=None)
    otaskid=models.CharField(max_length=255,primary_key=True)
    #otaskpath=models.CharField(max_length=255)

class BoundingBoxObject(models.Model):
    x=models.CharField(max_length=255)
    y=models.CharField(max_length=255)
    l=models.CharField(max_length=255)
    h=models.CharField(max_length=255)
    taskid=models.CharField(max_length=255)
    taskurl = models.CharField(max_length=2000)

    # bb_taskpath = models.ForeignKey(TaskPathBoundingBox, on_delete=models.CASCADE)
    # taskcode=models.CharField(max_length=255)
