from django.contrib import admin
from .models import TaskPath, TaskProcessedData

# Register your models here.
admin.site.register(TaskPath)
admin.site.register(TaskProcessedData)