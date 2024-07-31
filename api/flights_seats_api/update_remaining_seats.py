from redis import Redis
redis = Redis(host='localhost', port=6379, decode_responses=True)


def update_remaining_seats_func(flight_id, state):
    last = redis.get(f"flight_{flight_id}")
    if state == "buy":
        redis.set(f"flight_{flight_id}", last-1)
    else:
        redis.set(f"flight_{flight_id}", last + 1)
