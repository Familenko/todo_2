import datetime

from django.test import TestCase

from app.forms import TagForm, TaskForm
from app.models import Tag, Task


class Test(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            content="Test content",
            deadline=datetime.datetime.now() + datetime.timedelta(days=1),
        )

        self.tag = Tag.objects.create(
            name="Test tag",
        )

    def test_task_form(self):
        form = TaskForm(data={
            "content": "Test content",
            "deadline": datetime.datetime.now() + datetime.timedelta(days=1),
            "tags": [self.tag],
        })
        self.assertTrue(form.is_valid())

    def test_tag_form(self):
        form = TagForm(data={
            "name": "Test tag",
        })
        self.assertTrue(form.is_valid())

    def test_task_form_content(self):
        form = TaskForm(data={
            "content": "",
            "deadline": datetime.datetime.now() + datetime.timedelta(days=1),
            "tags": [self.tag],
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["content"], ["This field is required."])
