from django.urls import path

from . import views as adminportal_views

urlpatterns = [
    path('', adminportal_views.TaskListCreateAPIView.as_view()),

]
