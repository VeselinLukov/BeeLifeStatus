from django.urls import path

from beehives.views import beehives_list_view, BeehiveCreateView, BeehiveUpdateView, BeehiveDeleteView

app_name = 'beehives'
urlpatterns = [
    path('', beehives_list_view, name='beehives-list'),
    path('create/', BeehiveCreateView.as_view(), name='beehive-create'),
    path('edit/<int:pk>/', BeehiveUpdateView.as_view(), name='beehive-update'),
    path('delete/<int:pk>/', BeehiveDeleteView.as_view(), name='beehive-delete')
]