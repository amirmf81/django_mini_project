from myapp.models.flight_model import Flight


def get_flights_func(date):
    flights_id = Flight.get_date_flights(date=date)
    return flights_id
