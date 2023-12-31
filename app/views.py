from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from app.forms import TaskForm, TagForm
from app.models import Task, Tag


def complete_undo(request, pk):
    task = get_object_or_404(Task, id=pk)

    if task.done:
        task.done = False
    else:
        task.done = True
    task.save()

    return HttpResponseRedirect(reverse_lazy("app:task-list"))


class TaskListView(ListView):
    model = Task
    template_name = "app/task_list.html"
    context_object_name = "tasks"
    paginate_by = 10
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("app:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "app/tag_list.html"
    context_object_name = "tags"
    paginate_by = 10


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("app:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")
