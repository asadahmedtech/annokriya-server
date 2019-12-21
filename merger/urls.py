from django.contrib import admin
from django.urls import path
# from customers import views
from django.conf.urls import url, include
from . import views as v
# from backgroundprocess.views import distributorStatus

urlpatterns = [
    path('',v.callMerger),
    path('print_db/',v.callPrinter),
    path('bounding-box/',v.callMergerBoundingBox),
    path('bounding-box/print_db/',v.callPrinterBoundingBox),
]
