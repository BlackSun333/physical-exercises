from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import TaskForm

from .models import Task, Worker, Position, TaskType


def index(request):
    context = {
        "task_count": Task.objects.count(),
        "worker_count": Worker.objects.count(),
        "completed_tasks": Task.objects.filter(is_completed=True).count(),
        "task_types_count": TaskType.objects.count(),
    }
    return render(request, "catalog/index.html", context)



class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task-list")



class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 10


class WorkerDetailView(generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    fields = ("username", "first_name", "last_name", "email", "position", "password")
    success_url = reverse_lazy("worker-list")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    fields = ("username", "first_name", "last_name", "email", "position")
    success_url = reverse_lazy("worker-list")


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("worker-list")