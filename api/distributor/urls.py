from django.urls import path

from . import views as task_distributor_views

urlpatterns = [
    path('get/<int:pk>', task_distributor_views.getTask.as_view()),
    path('post/', task_distributor_views.postTask.as_view()),
]
