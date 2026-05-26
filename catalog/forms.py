from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Task, Worker


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = Task
        fields = "__all__"


class WorkerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email", "position")


class WorkerUpdateForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "position")