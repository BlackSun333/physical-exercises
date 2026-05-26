from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, Worker, TaskType
from .forms import TaskForm, WorkerCreationForm, WorkerUpdateForm


def index(request):
    context = {
        "task_count": Task.objects.count(),
        "worker_count": Worker.objects.count(),
        "completed_tasks": Task.objects.filter(is_completed=True).count(),
        "task_types_count": TaskType.objects.count(),
    }
    return render(request, "catalog/index.html", context)


# Auth Views

class WorkerLoginView(LoginView):
    template_name = "catalog/login.html"
    redirect_authenticated_user = True


class WorkerLogoutView(LogoutView):
    next_page = "login"


# Task Views

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")


# Worker Views

class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("login")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("worker-list")
