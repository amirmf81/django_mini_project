from myapp.models.user_model import User


class PassengerInformation:
    def __init__(self, passenger_id):
        self.passenger = User.get_user(user_id=passenger_id)

    def make(self):
        information = {
            "first_name": self.passenger.name,
            "last_name": self.passenger.last_name,
            "gender": self.passenger.gender,
            "national_id_number": self.passenger.national_id_number,
            "birth_date": str(self.passenger.birth_date),
        }
        return information
