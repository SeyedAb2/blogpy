from django.conf.urls import url , include
from django.urls import path , re_path

from blog import views

urlpatterns = [
    re_path(r'^$', views.IndexPage.as_view(),name = 'index'),
    re_path(r'^contact/$', views.ContactPage.as_view(),name = 'contact'),
    re_path(r'^about/$', views.AboutUs.as_view(),name = 'about'),
]