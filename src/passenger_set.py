class PassengerSet:
    def __init__(self):
        self.passengers = set()

    def count_passengers(self):
        return len(self.passengers)
    
    def add_to_set(self, passenger):
        self.passengers.add(passenger)

    def remove_from_set(self, passenger):
        self.passengers.remove(passenger)
    
    def clear(self):
        self.passengers.clear()

    def get_passenger_list(self):
        return list(self.passengers)