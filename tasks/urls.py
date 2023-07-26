from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('add_task/', views.add_task, name='add_task'),

    path('bulk_add/', views.bulk_add_tasks, name='bulk_add_tasks'),
    path('bulk_delete/', views.bulk_delete_tasks, name='bulk_delete_tasks'),
]
