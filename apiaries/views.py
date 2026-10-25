from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import context

from apiaries.models import Apiary


def home_view(request: HttpRequest) -> HttpResponse:
    total_apiaries_count = Apiary.objects.count()
    last_added_apiary = Apiary.objects.order_by('-created_at').first()

    context = {
        'total_apiaries_count': total_apiaries_count,
        'last_added_apiary': last_added_apiary,
        'page_title': 'Home',
    }

    return render(request, 'apiaries/home.html', context)
