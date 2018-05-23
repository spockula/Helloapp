from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
	path('', views.index, name = 'index'),
]