from django import forms

from tasks.models import Task


class TasksBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['inspection']

        labels = {
            'task_title': "Task title",
            'task_description': "Task description",
            'deadline': "Deadline",
            'task_status': "Task status",
        }

        widgets = {
            'task_title': forms.TextInput(attrs={'placeholder': 'Insert task title'}),
            'task_description': forms.Textarea(attrs={
                'placeholder': 'Insert task description'
            }),
            'deadline': forms.SelectDateWidget(),
            'task_status': forms.Select(),
        }

        error_messages = {
            'task_title': {
                'unique': 'Task title should be unique!',
            }
        }


class TasksCreateForm(TasksBaseForm):
    class Meta(TasksBaseForm.Meta):
        help_texts = {
            'task_title': "Write unique task title",
            'task_description': "Add task description (optional)",
            'deadline': "Choose deadline date",
            'task_status': "Choose task status",
        }


class TasksUpdateForm(TasksBaseForm):
    class Meta(TasksBaseForm.Meta):
        widgets = {
            'task_title': forms.TextInput(attrs={
                'placeholder': 'Insert task title',
                'disabled': 'disabled',
            }),
            'task_description': forms.Textarea(attrs={
                'placeholder': 'Insert task description'
            }),
            'deadline': forms.SelectDateWidget(),
            'task_status': forms.Select(),
        }

        help_texts = {
            'task_title': "You can't change your task title",
            'task_description': "Add task description (optional)",
            'deadline': "Choose deadline date",
            'task_status': "Choose task status",
        }


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
    )
