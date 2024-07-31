from django.http import JsonResponse
from api.admin_api.get_passengers_information.get_tickets import get_tickets_func
from api.admin_api.get_passengers_information.get_passengers import get_passengers_func
from api.admin_api.get_passengers_information.information_handler import information_handler_func


def get_passengers_information_func(flight_id, page):
    tickets_id = get_tickets_func(flight_id, page)
    passengers_id = get_passengers_func(tickets_id=tickets_id)
    information = information_handler_func(passengers_id=passengers_id)
    return JsonResponse({
        "ok": True,
        "passengers": information,
    })

