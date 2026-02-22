from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from django.db.models import Q


def landingPageView(request):
    if request.user.is_authenticated:
        return redirect('task-list')  # your task list view
    return render(request, 'home.html')

class TaskListView(LoginRequiredMixin,ListView):
    model= Task
    template_name = 'tasklist.html'
    context_object_name = 'tasks'
    ordering = ['-priority','-created_date']
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        user=self.request.user
        if user is not None:
            queryset = queryset.filter(Q(category__type="WORK") | Q(category__type="PERSONAL") & Q(creator=user))
        user_param=self.kwargs.get('creator_id')
        if user_param is not None:
            queryset = queryset.filter(creator=user_param)
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
    form_class = TaskForm
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model=Task
    template_name = 'taskcreate.html'
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    template_name = 'deleteConfirmation.html'
    success_url = reverse_lazy('task-list')
    success_message = 'The task is deleted'










