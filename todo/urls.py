from django.urls import path
from .views import home, CreateTaskView, TaskListView, TaskStatusUpdate

urlpatterns = [
    path('', home, name='todo-home'),
    path('createtask/', CreateTaskView.as_view(), name='create-task'),
    path('usertasks/', TaskListView.as_view(), name='task-list'),
    path('usertasks/<int:pk>', TaskStatusUpdate.as_view(), name='update-status'),
]