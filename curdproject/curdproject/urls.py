"""curdproject URL Configuration

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
from django.conf.urls import url
from curdapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^create',views.product_insert_view),
    url(r'^retrieve',views.product_retrieve_view),
    url(r'^update',views.product_update_view),
    url(r'^delete',views.product_delete_view)
]



