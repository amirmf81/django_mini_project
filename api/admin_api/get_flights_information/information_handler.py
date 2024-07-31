from api.admin_api.get_flights_information.make_flight_information import FlightInformation


def information_handler_func(flights: list, page):
    all_information = []
    for flight_id in flights:
        flight_information = FlightInformation(
            flight_id=flight_id,
        ).start()
        all_information.append(flight_information)
    ans_information = []
    for i in range(10 * (page - 1), 10 * page):
        ans_information.append(all_information[i])
    return ans_information

