from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home', views.home , name='home'),
    path('view/<int:id>', views.view_books , name='view_books'),
    path('create', views.create , name='create'),
     path('update', views.update ,name='update'),
     path('update_book', views.update_book ,name='update_book'),
    

    
]
