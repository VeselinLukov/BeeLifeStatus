from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages

from inspections.forms import InspectionCreateForm, InspectionUpdateForm
from inspections.models import Inspection


def inspections_list_view(request: HttpRequest) -> HttpResponse:
    inspections = Inspection.objects.order_by('-inspection_date')

    context = {
        'inspections': inspections,
    }

    return render(request, 'inspections/inspections_list.html', context)


class InspectionCreateView(CreateView):
    model = Inspection
    form_class = InspectionCreateForm
    success_url = reverse_lazy('inspections:inspections-list')

    def form_valid(self, form):
        messages.success(self.request, "Inspection log successfully created!")
        return super().form_valid(form)


class InspectionUpdateView(UpdateView):
    model = Inspection
    form_class = InspectionUpdateForm
    success_url = reverse_lazy('inspections:inspections-list')


class InspectionDeleteView(DeleteView):
    model = Inspection
    success_url = reverse_lazy('inspections:inspections-list')
