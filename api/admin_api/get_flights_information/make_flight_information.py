from myapp.models.flight_model import Flight
from api.flights_seats_api.get_remaining_seats import get_remaining_seats_func


class FlightInformation:
    def __init__(self, flight_id):
        self.flight = Flight.objects.get(id=flight_id)

    def start(self):
        information = {
            "airline": self.flight.owner.name,
            "origin": self.flight.origin,
            "destination": self.flight.destination,
            "take_off_time": self.flight.take_off_time,
            "landing_time": self.flight.landing_time,
            "price": self.flight.price,
            "remaining_seats": get_remaining_seats_func(self.flight.id),
        }
        return information

