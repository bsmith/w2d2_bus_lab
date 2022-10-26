from .passenger_set import PassengerSet
from .delegatetools import delegate

class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = PassengerSet()

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return self.passengers.count_passengers()

    # def pick_up(self, person):
    #     self.passengers.add_to_set(person)
    pick_up = delegate("passengers", "add_to_set")

    def drop_off(self, person):
        self.passengers.remove_from_set(person)

    def empty(self):
        for person in self.passengers.get_passenger_list():
            self.drop_off(person)

    def pick_up_from_stop(self, bus_stop):
        new_passengers = bus_stop.queue.get_passenger_list()
        bus_stop.clear()
        for person in new_passengers:
            self.pick_up(person)
        