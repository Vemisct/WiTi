from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'TaskList.html'
    context_object_name = 'taskslist'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'TaskCreate.html'
    
    success_url = '/task/catalog/all/'
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)