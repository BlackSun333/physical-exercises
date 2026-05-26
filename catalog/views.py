from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Task, Worker, TaskType
from .forms import TaskForm, WorkerCreationForm, WorkerUpdateForm


class ManagerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        user = self.request.user
        return (
            user.is_authenticated
            and user.position is not None
            and user.position.name.lower() == "manager"
        )


def index(request):
    context = {
        "task_count": Task.objects.count(),
        "worker_count": Worker.objects.count(),
        "completed_tasks": Task.objects.filter(is_completed=True).count(),
        "task_types_count": TaskType.objects.count(),
    }
    return render(request, "catalog/index.html", context)


class WorkerLoginView(LoginView):
    template_name = "catalog/login.html"
    redirect_authenticated_user = True


class WorkerLogoutView(LogoutView):
    next_page = "login"


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


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(ManagerRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("worker-list")


class WorkerUpdateView(ManagerRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("worker-list")


class WorkerDeleteView(ManagerRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("worker-list")