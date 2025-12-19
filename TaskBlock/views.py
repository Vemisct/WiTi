from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import TaskForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import *
from django.contrib.auth.forms import *
from django.contrib.auth import *

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

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        comment_text = request.POST.get('text')
        
        if comment_text and request.user.is_authenticated:
            Comment.objects.create(
                task=task,
                author=request.user,
                text=comment_text
            )
        return redirect('WTTaskDetail', pk=task.pk)
    

class LogINView(LoginView):
    template_name = 'LogIN.html'
    redirect_authenticated_user = True


class LogOUTView(LogoutView):
    next_page = 'WTTaskList'

class RegisterView(CreateView):
    template_name = 'Register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('WTTaskList')

    def form_valid(self, form):
        reguser = form.save()
        login(self.request, reguser)
        return super().form_valid(form)