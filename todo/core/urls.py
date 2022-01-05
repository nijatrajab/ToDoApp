from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('remove_task/', views.remove_task, name='remove_task'),
    path('check_task/', views.check_task, name='check_task'),
    path('check_all_tasks/', views.check_all_tasks, name='check_all_tasks'),
    path('remove_all_tasks/', views.remove_all_tasks, name='remove_all_tasks'),
    path('remove_all_checked_tasks/', views.remove_all_checked_tasks, name='remove_all_checked_tasks'),
]
