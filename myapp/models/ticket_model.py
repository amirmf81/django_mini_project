from django.db import models
from myapp.models.flight_model import Flight
from myapp.models.user_model import User


class Ticket(models.Model):
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def get_tickets(cls, flight_id):
        return list(Ticket.objects.filter(flight_id=flight_id).id)

    @classmethod
    def get_passenger(cls, ticket_id):
        return Ticket.objects.get(id=ticket_id).owner.id
