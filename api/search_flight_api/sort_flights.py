from myapp.models.flight_model import Flight


def sort_flights_func(flights_id: list):
    price_id_list = []
    for flight_id in flights_id:
        temp_price = Flight.get_price(flight_id=flight_id)
        price_id_list.append([temp_price, flight_id])
    price_id_list.sort()
    ans_flights_id = []
    for price_id in price_id_list:
        ans_flights_id.append(price_id[1])
    return ans_flights_id
