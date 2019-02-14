from django.conf.urls import url
from django.urls import path, re_path

from blog import views

urlpatterns= [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^posts/$', views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>', views.PostDetailView, name='post_detail'),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^projects/$', views.ProjectPageView.as_view()),
    url(r'^resume/$', views.ResumePageView.as_view()),
    url(r'^contact/$', views.ContactPageView.as_view()),
]
