from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from tasks.forms import SearchForm, TasksCreateForm, TasksUpdateForm
from tasks.models import Task


def tasks_list_view(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().prefetch_related('inspection').order_by('deadline')
    search_form = SearchForm(request.GET or None)

    if request.GET and search_form.is_valid():
        tasks = tasks.filter(task_title__icontains=search_form.cleaned_data['query'])

    context = {
        'tasks': tasks,
        'search_form': search_form,
    }
    return render(request, 'tasks/tasks_list.html', context)


class TasksCreateView(CreateView):
    model = Task
    form_class = TasksCreateForm
    success_url = reverse_lazy('tasks:tasks-list')

    def form_valid(self, form):
        messages.success(self.request, "Inspection log successfully created!")
        return super().form_valid(form)


class TasksUpdateView(UpdateView):
    model = Task
    form_class = TasksUpdateForm
    success_url = reverse_lazy('tasks:tasks-list')


class TasksDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:tasks-list')
