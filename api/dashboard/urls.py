from django.urls import path

from . import views as dashboard_views

urlpatterns = [
    path('', dashboard_views.UserDashboard.as_view()),

]
