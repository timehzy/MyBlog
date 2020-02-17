from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index.html/', views.index),
    path('artical/<artical_id>/', views.artical_page, name='artical_page'),
    path('edit_page/<artical_id>/', views.edit_page, name='edit_page'),
    path('edit_submit/', views.edit_submit, name='edit_submit'),
]
