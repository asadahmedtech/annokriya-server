from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.contrib.auth.models import BaseUserManager
# Create your models here.

class TaskPath(models.Model):
    taskgivenID = models.CharField(max_length=255, primary_key=True)
    # taskPath = models.CharField(max_length=255)
    taskPath = models.ImageField(upload_to='post_images')
    taskCount = models.IntegerField(default = 0)

    def __str__(self):
    	return "{}".format(self.taskgivenID)

class TaskProcessedData(models.Model):
    taskpath = models.ForeignKey(TaskPath, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    x1=models.CharField(max_length=255)
    x2=models.CharField(max_length=255)
    x3=models.CharField(max_length=255)
    x4=models.CharField(max_length=255)
    x5=models.CharField(max_length=255)

    y1=models.CharField(max_length=255)
    y2=models.CharField(max_length=255)
    y3=models.CharField(max_length=255)
    y4=models.CharField(max_length=255)
    y5=models.CharField(max_length=255)

    def __str__(self):
    	return "{}-{}".format(str(self.taskpath), self.user.pk)
