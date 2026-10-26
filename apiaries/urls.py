from django.urls import path

from .views import home_view, ApiaryCreateView, ApiaryUpdateView, ApiaryDeleteView

app_name = 'apiaries'

urlpatterns = [
    path('', home_view, name='home-page'),
    path('create/', ApiaryCreateView.as_view(), name='apiary-create'),
    path('edit/<int:pk>/', ApiaryUpdateView.as_view(), name='apiary-update'),
    path('delete/<int:pk>/', ApiaryDeleteView.as_view(), name='apiary-delete')
]