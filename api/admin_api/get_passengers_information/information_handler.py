from api.admin_api.get_passengers_information.make_passenger_information import PassengerInformation


def information_handler_func(passengers_id):
    information = []
    for passenger_id in passengers_id:
        passenger_information = PassengerInformation(
            passenger_id=passenger_id,
        ).make()
        information.append(passenger_information)
    return information

