from django.shortcuts import render
from django.views import generic
from .models import Task, Worker


def index(request):
    context = {
        "task_count": Task.objects.count(),
        "worker_count": Worker.objects.count(),
        "completed_tasks": Task.objects.filter(is_completed=True).count(),
    }
    return render(request, "catalog/index.html", context)


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskDetailView(generic.DetailView):
    model = Task


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 10


class WorkerDetailView(generic.DetailView):
    model = Worker
