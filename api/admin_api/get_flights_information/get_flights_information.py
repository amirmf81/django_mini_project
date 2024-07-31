from django.http import JsonResponse
from api.admin_api.get_flights_information.information_handler import information_handler_func
from api.admin_api.get_flights_information.get_flights import get_flights_func
from django.utils.dateparse import parse_date


def get_flights_information_func(date_str, page):
    date = parse_date(date_str)
    flights = get_flights_func(date=date)
    information = information_handler_func(
        flights=flights,
        page=page
    )
    return JsonResponse({
        "ok": True,
        "flights": information,
    })

