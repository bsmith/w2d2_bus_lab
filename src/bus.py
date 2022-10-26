from .delegatetools import delegate

class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = set()

    def drive(self):
        return "Brum brum"

    # def passenger_count(self):
    #     return self.passengers.count_passengers()
    # passenger_count = delegate("passengers", "length")
    def passenger_count(self):
        return len(self.passengers)

    # def pick_up(self, person):
    #     self.passengers.add_to_set(person)
    pick_up = delegate("passengers", "add")

    # def drop_off(self, person):
    #     self.passengers.remove_from_set(person)
    drop_off = delegate("passengers", "remove")

    # def empty(self):
    #     for person in self.passengers.get_passenger_list():
    #         self.drop_off(person)
    empty = delegate("passengers", "clear")

    def pick_up_from_stop(self, bus_stop):
        # new_passengers = bus_stop.queue
        # for person in new_passengers:
        #     self.pick_up(person)
        # bus_stop.clear()
        bus_queue = bus_stop.queue
        while len(bus_queue) > 0:
            self.pick_up(bus_queue.pop())
