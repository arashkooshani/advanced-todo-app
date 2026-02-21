from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(ListView):
    model= Task
    template_name = 'tasklist.html'
    context_object_name = 'tasks'
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        creator=self.kwargs.get('creator')
        if creator:
            queryset = queryset.filter(creator=creator)
        completed=self.request.GET.get('completed')
        if completed:
            queryset = queryset.filter(completed=completed)
        return queryset

class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskdetail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'taskcreate.html'
    fields = ['title', 'description','due_date']
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model=Task
    template_name = 'taskcreate.html'
    fields = ['title', 'description','due_date','completed']
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    template_name = 'deleteConfirmation.html'
    success_url = reverse_lazy('task-list')
    success_message = 'The task is deleted'








