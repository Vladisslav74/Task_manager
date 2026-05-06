from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('completed/', views.Completed),
    path('urgent/', views.Urgent),
    path('delete/<int:pk>/', views.delete, name='delete_task'),
]









