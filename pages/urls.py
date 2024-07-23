from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.pages, name='pages'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('products/', include('products.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
]
