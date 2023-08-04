# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
]
