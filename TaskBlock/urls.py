from django.urls import path
from .views import *

urlpatterns = [
    path('task/catalog/all/', TaskListView.as_view(), name='WTTaskList'),
    path('task/create/', TaskCreateView.as_view(), name='WTTaskCreate'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='WTTaskUpdate'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='WTTaskDelete'),
    path('task/detail/<int:pk>/', TaskDetailView.as_view(), name='WTTaskDetail'),
]