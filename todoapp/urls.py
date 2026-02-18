
from django.urls import path
from .views import TaskListView,TaskDetailView,TaskCreateView

urlpatterns = [
    path('', TaskListView.as_view(),name='task-list'),
    path('creator/<int:creator_id>', TaskListView.as_view(),name='task-list-creator'),
    path('task/<int:pk>', TaskDetailView.as_view(),name='task-detail'),
    path('task/create/', TaskCreateView.as_view(),name='task-create'),
]