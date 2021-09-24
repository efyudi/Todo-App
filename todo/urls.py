from django.urls import path
from .views import TodoListView, AddTaskCreateView, update_task, DeleteTask

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_home'),
    path('add-task/', AddTaskCreateView.as_view(), name='add_task'),
    path('update-task/<pk>/', update_task, name='update_task'),
    path('delete-task/<pk>/', DeleteTask.as_view(), name='delete_task')
]
