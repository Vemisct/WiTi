from django.urls import path
from .views import *

urlpatterns = [
    path('task/catalog/all/', TaskListView.as_view(), name='WTTaskList'),
    path('task/create/', TaskCreateView.as_view(), name='WTTaskCreate'),
]