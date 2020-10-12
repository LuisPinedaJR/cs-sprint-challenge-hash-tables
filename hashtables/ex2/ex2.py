#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    ticket_hash = {}

    for ticket in tickets:
        ticket_hash[ticket.source] = ticket.destination

    source = "NONE"
    for i in range(length):
        route.append(ticket_hash[source])
        source = ticket_hash[source]
        
    return route
