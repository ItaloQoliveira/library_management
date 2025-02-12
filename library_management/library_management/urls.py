"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books.views import *

urlpatterns = [
    path('books/', book_list, name= 'book_list'),
    path('books/<int:pk>/', book_detail, name= 'book_detail"'),
    path('books/create/', book_create, name= 'book_create'),
    path('books/<int:pk>/update', book_update, name= 'book_update'),
    path('books/<int:pk>/delete', book_delete, name= 'book_delete'),

]