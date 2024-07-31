from django.http import JsonResponse

from myapp.models.airline_model import Airline


def create_airline_view_func(request):
    name = request.POST.get("name")
    return JsonResponse({
        "ok": Airline.create(name=name),
    })

