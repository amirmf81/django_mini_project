from myapp.models.flight_model import Flight
from django.utils.dateparse import parse_date
from api.flights_seats_api.get_remaining_seats import get_remaining_seats_func


def get_flights_func(origin, destination, date, passengers_number):
    ans_flights_id = []
    all_flights_id = Flight.search_flight(
        origin=origin,
        destination=destination,
        date=parse_date(date),
    )
    for flight_id in all_flights_id:
        remaining_seats = get_remaining_seats_func(flight_id=flight_id)
        if remaining_seats >= passengers_number:
            ans_flights_id.append(flight_id)
    return ans_flights_id
