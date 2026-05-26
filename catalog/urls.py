from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # Tasks
    path("tasks/", views.TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),

    # Workers
    path("workers/", views.WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", views.WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", views.WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", views.WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", views.WorkerDeleteView.as_view(), name="worker-delete"),
]
