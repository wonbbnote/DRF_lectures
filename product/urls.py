from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns =[
    path('', views.ProductView.as_view()),
    path('<int:id>', views.ProductView.as_view()),
    
]