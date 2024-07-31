from redis import Redis
from myapp.models.flight_model import Flight
redis = Redis(host='localhost', port=6379, decode_responses=True)


def set_remaining_seats_func(flight_id):
    redis.set(f"flight_{flight_id}", Flight.get_seats_number(flight_id=flight_id))
