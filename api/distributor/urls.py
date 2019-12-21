from django.urls import path

from . import views as task_distributor_views

urlpatterns = [
    path('get/<int:pk>', task_distributor_views.getTask.as_view()),
    path('post/', task_distributor_views.postTask.as_view()),

    path('get/bb/<int:pk>', task_distributor_views.getTaskBoundingBox.as_view()),
    path('post/bb/', task_distributor_views.postTaskBoundingBox.as_view()),

]
