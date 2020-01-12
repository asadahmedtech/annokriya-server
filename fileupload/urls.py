from django.urls import path
from django.conf.urls import url, include

from . import views as v

urlpatterns = [
    path('',v.image_upload,name='upload'),
]
