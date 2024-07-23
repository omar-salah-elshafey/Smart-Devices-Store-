from . import views
from django.urls import path

urlpatterns = [
    path('', views.phones, name='phones'),
    path('tablets/', views.tablets, name='tablets'),
    path('watches/', views.watches, name='watches'),
    path('airpods/', views.airpods, name='airpods'),
    path('phone_detail/<str:phone_name>/',
         views.phone_detail, name='phone_detail'),
    path('tab_detail/<str:tab_name>/', views.tab_detail, name='tab_detail'),
    path('watch_detail/<str:watch_name>/',
         views.watch_detail, name='watch_detail'),
    path('airpod_detail/<str:airpod_name>/',
         views.airpod_detail, name='airpod_detail'),
]
