from myapp.models.ticket_model import Ticket


def get_tickets_func(flight_id, page):
    all_tickets_id = Ticket.get_tickets(flight_id=flight_id)
    ans_tickets_id = []
    for i in range(10 * (page - 1), 10 * page):
        ans_tickets_id.append(all_tickets_id[i])
    return ans_tickets_id
