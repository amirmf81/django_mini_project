from redis import Redis
redis = Redis(host='localhost', port=6379, decode_responses=True)


def get_remaining_seats_func(flight_id):
    return redis.get(f"flight_{flight_id}")
