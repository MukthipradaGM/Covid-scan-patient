from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('report', views.report,name='report'),
    path('generate_report', views.generate_report,name='generate_report'),
    path('download_report', views.download_report,name='download_report'),       
]
