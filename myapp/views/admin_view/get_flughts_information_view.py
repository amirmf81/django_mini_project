from api.admin_api.get_flights_information.get_flights_information import get_flights_information_func


def get_flights_information_view_func(request):
    date = request.POST.get("date")
    page = request.POST.get("page")
    return get_flights_information_func(
        date_str=date,
        page=page,
    )
