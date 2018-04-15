from django.conf.urls import url
from howdy import views
from django.urls import path

urlpatterns= [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^projects/$', views.ProjectPageView.as_view()),
    url(r'^resume/$', views.ResumePageView.as_view()),
    url(r'^contact/$', views.ContactPageView.as_view()),
]