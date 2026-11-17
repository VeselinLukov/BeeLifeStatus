from django.urls import path

from tasks.views import tasks_list_view, TasksCreateView, TasksUpdateView, TasksDeleteView

app_name = 'tasks'
urlpatterns = [
    path('', tasks_list_view, name='tasks-list'),
    path('create/', TasksCreateView.as_view(), name='task-create'),
    path('edit/<int:pk>/', TasksUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>/', TasksDeleteView.as_view(), name='task-delete')
]
