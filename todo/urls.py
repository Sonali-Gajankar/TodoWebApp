from django.urls import path
from .views import home, about, CreateTaskView, TaskListView, TaskStatusUpdate, TaskUpdateView

urlpatterns = [
    path('', home, name='todo-home'),
    path('about/', about, name='about'),
    path('createtask/', CreateTaskView.as_view(), name='create-task'),
    path('usertasks/', TaskListView.as_view(), name='task-list'),
    path('usertasks/<str:days>', TaskListView.as_view(), name='task-list'),
    path('usertasks/status/<int:pk>', TaskStatusUpdate.as_view(), name='update-status'),
    path('usertasks/update/<int:pk>', TaskUpdateView.as_view(), name='update')
]