# Generated by Django 4.2.7 on 2023-11-27 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 4, 9, 20, 20, 280094, tzinfo=datetime.timezone.utc), null=True)),
                ('done', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(blank=True, related_name='tasks', to='app.tag')),
            ],
            options={
                'ordering': ['done', 'datetime'],
            },
        ),
    ]
