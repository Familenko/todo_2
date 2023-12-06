from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

from app.models import Task, Tag


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
