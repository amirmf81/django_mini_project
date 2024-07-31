from myapp.models.ticket_model import Ticket


def get_passengers_func(tickets_id):
    passengers_id = []
    for ticket_id in tickets_id:
        passengers_id.append(Ticket.get_passenger(ticket_id=ticket_id))
    return passengers_id
