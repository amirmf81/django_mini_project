from api.search_flight_api.search_flight import search_flight_func


def search_flight_view_func(request):
    origin = request.POST.get("origin")
    destination = request.POST.get("destination")
    date = request.POST.get("date")
    passengers_number = request.POST.get("passengers_number")
    sort = request.POST.get("sort")
    page = request.POST.get("page")
    return search_flight_func(
        origin=origin,
        destination=destination,
        date=date,
        passengers_number=passengers_number,
        sort=sort,
        page=page,
    )
