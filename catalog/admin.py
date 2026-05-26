from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Position, Task, TaskType, Worker


@admin.register(Worker)
class WorkerAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )
    list_display = ("username", "first_name", "last_name", "email", "position", "is_staff")
    list_filter = UserAdmin.list_filter + ("position",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "priority", "deadline", "is_completed", "task_type")
    list_filter = ("priority", "is_completed", "task_type")
    search_fields = ("name",)
    filter_horizontal = ("assignees",)