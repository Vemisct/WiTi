from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect

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
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'TaskUpdate.html'
    
    success_url = '/task/catalog/all/'

class TaskDeleteView(DeleteView):
    model = Task
    
    success_url = '/task/catalog/all/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return HttpResponseRedirect(self.get_success_url())
    
class TaskDetailView(DetailView):
    model = Task
    template_name = 'TaskDetail.html'
    context_object_name = "task"