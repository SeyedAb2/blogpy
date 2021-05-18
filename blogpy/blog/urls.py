from django.conf.urls import url , include
from django.urls import path , re_path

from blog import views

urlpatterns = [
    re_path(r'^$', views.IndexPage.as_view(),name = 'index')
]