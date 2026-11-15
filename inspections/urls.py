from django.urls import path

from inspections.views import inspections_list_view, InspectionCreateView, InspectionUpdateView, InspectionDeleteView

app_name = 'inspections'
urlpatterns = [
    path('', inspections_list_view, name='inspections-list'),
    path('create/', InspectionCreateView.as_view(), name='inspection-create'),
    path('edit/<int:pk>/', InspectionUpdateView.as_view(), name='inspection-update'),
    path('delete/<int:pk>/', InspectionDeleteView.as_view(), name='inspection-delete')
]
