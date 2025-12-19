from django.urls import path
from .views import *

urlpatterns = [
    path('wt/task/catalog/all/', TaskListView.as_view(), name='WTTaskList'),
    path('wt/task/create/', TaskCreateView.as_view(), name='WTTaskCreate'),
    path('wt/task/update/<int:pk>/', TaskUpdateView.as_view(), name='WTTaskUpdate'),
    path('wt/task/delete/<int:pk>/', TaskDeleteView.as_view(), name='WTTaskDelete'),
    path('wt/task/detail/<int:pk>/', TaskDetailView.as_view(), name='WTTaskDetail'),
    path('wt/user/login/', LogINView.as_view(), name='WTUserLogin'),
    path('wt/user/logout/', LogOUTView.as_view(), name='WTUserLogout'),
    path('wt/user/register/', RegisterView.as_view(), name='WTUserRegister'),
]