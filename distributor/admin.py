from django.contrib import admin
from .models import TaskPath, TaskProcessedData, TaskPathBoundingBox, TaskProcessedDataBoundingBox

# Register your models here.
admin.site.register(TaskPath)
admin.site.register(TaskProcessedData)
admin.site.register(TaskPathBoundingBox)
admin.site.register(TaskProcessedDataBoundingBox)
