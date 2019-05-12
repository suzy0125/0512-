from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('new/', views.post_new, name='new'),
    path('detail/<int:post_id>/edit/', views.post_edit, name='edit'),
    path('detail/<int:post_id>/delete/', views.post_delete, name='delete'),
]