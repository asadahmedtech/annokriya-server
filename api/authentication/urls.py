from django.urls import path

from . import views as authentication_views

urlpatterns = [
    path('register', authentication_views.UserSignUpView.as_view()),
    path('profile', authentication_views.UserUpdateProfile.as_view()),
    path('login', authentication_views.UserLogin.as_view()),
     path("login2", authentication_views.LoginAPI.as_view()),
    # path('profile/(?P<pk>[0-9]+)', authentication_views.UserUpdateProfile.as_view()),
]
