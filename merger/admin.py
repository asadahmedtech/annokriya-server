from django.contrib import admin
from .models import OutputTable, BoundingBoxObject, BoundingBoxObjectnew, BoundingBoxObjectallnew
# Register your models here.
admin.site.register(OutputTable)
admin.site.register(BoundingBoxObject)
admin.site.register(BoundingBoxObjectnew)
admin.site.register(BoundingBoxObjectallnew)