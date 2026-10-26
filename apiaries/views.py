from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from apiaries.forms import ApiaryBaseForm
from apiaries.models import Apiary


def home_view(request: HttpRequest) -> HttpResponse:
    total_apiaries_count = Apiary.objects.count()
    apiaries = Apiary.objects.order_by('-created_at')

    context = {
        'total_apiaries_count': total_apiaries_count,
        'apiaries': apiaries,
        'page_title': 'Home',
    }

    return render(request, 'apiaries/home.html', context)


class ApiaryCreateView(CreateView):
    model = Apiary
    form_class = ApiaryBaseForm
    success_url = reverse_lazy('apiaries:home-page')

    def valid_form(self, form):
        messages.success(self.request, "Apiary successfully created.")
        return super().valid_form(form)


class ApiaryUpdateView(UpdateView):
    model = Apiary
    form_class = ApiaryBaseForm
    success_url = reverse_lazy('apiaries:home-page')


class ApiaryDeleteView(DeleteView):
    model = Apiary
    success_url = reverse_lazy('apiaries:home-page')
