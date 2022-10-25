from .passenger_set import PassengerSet

class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = PassengerSet()

    def queue_length(self):
        return self.queue.count_passengers()

    def add_to_queue(self, person):
        self.queue.add_to_set(person)

    def clear(self):
        self.queue.clear()