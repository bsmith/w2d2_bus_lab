class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        for person in self.passengers:
            self.drop_off(person)

    def pick_up_from_stop(self, bus_stop):
        new_passengers = bus_stop.queue
        bus_stop.clear()
        for person in new_passengers:
            self.pick_up(person)
        