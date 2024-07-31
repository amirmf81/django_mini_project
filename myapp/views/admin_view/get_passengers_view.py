from api.admin_api.get_passengers_information.get_passengers_information import get_passengers_information_func


def get_passengers_view_func(request):
    flight_id = request.POST.get("flight_id")
    page = request.POST.get("page")
    return get_passengers_information_func(flight_id=flight_id, page=page)
