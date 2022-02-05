from django.urls import re_path, include
from . import views

urlpatterns=[
    re_path(r'^$', views.index, name='index'),
    re_path(r'^TSassigned$', views.TSassigned, name='TSassigned'),
    re_path(r'^TSdashboard$', views.TSdashboard, name='TSdashboard'),
    re_path(r'^TSproject$', views.TSproject, name='TSproject'),
    re_path(r'^TSprojectdetails$', views.TSprojectdetails, name='TSprojectdetails'),
    re_path(r'^TSsubmitted$', views.TSsubmitted, name='TSsubmitted'),
    re_path(r'^TStask$', views.TStask, name='TStask'),
    re_path(r'^TSsucess$', views.TSsucess, name='TSsucess'),
]