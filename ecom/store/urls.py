from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
]