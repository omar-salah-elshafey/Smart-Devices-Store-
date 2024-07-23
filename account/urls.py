from . import views
from django.urls import path

urlpatterns=[
    path('', views.account, name='account'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]