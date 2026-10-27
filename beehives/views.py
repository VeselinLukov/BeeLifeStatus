from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from beehives.forms import BeehiveBaseForm
from beehives.models import Beehive


def beehives_list_view(request: HttpRequest) -> HttpResponse:
    beehives = Beehive.objects.order_by('-installation_date')

    context = {
        'beehives': beehives,
    }

    return render(request, 'beehives/beehives_list.html', context)


class BeehiveCreateView(CreateView):
    model = Beehive
    form_class = BeehiveBaseForm
    success_url = reverse_lazy('beehives:beehives-list')

    def form_valid(self, form):
        messages.success(self.request, "Beehive successfully created.")
        return super().form_valid(form)


class BeehiveUpdateView(UpdateView):
    model = Beehive
    form_class = BeehiveBaseForm
    success_url = reverse_lazy('beehives:beehives-list')


class BeehiveDeleteView(DeleteView):
    model = Beehive
    success_url = reverse_lazy('beehives:beehives-list')
