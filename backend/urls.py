"""reactWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from customers import views
from django.conf.urls import url, include

# from backgroundprocess.views import distributorStatus

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth/user/', include('api.authentication.urls')),
    # path('^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^api/task/', include('api.distributor.urls')),
    # url(r'^background/', include('backgroundprocess.urls')),
    # url(r'^api/customers/$', views.customers_list),
    # url(r'^api/customers/(?P<pk>[0-9]+)$', views.customers_detail),
    # url(r'^',views.homePageView)

    url(r'^add_to_db/', include('merger.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('fileupload/',include('fileupload.urls')),
]

# distributorStatus(repeat=10, repeat_untill=None)