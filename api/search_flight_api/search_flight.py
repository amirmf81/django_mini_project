from django.http import JsonResponse
from api.search_flight_api.get_flights import get_flights_func
from api.search_flight_api.sort_flights import sort_flights_func
from api.admin_api.get_flights_information.information_handler import information_handler_func


def search_flight_func(origin, destination, date, passengers_number, sort, page):
    flights_id = get_flights_func(
        origin=origin,
        destination=destination,
        date=date,
        passengers_number=passengers_number,
    )
    sorted_flights = flights_id
    if sort:
        sorted_flights = sort_flights_func(flights_id=flights_id)
    information = information_handler_func(flights=sorted_flights, page=page)
    return JsonResponse({
        "ok": True,
        "flights": information,
    })
