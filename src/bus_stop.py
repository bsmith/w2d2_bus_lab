from .delegatetools import delegate

class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = list()

    def queue_length(self):
        return len(self.queue)

    # def add_to_queue(self, person):
    #     self.queue.add_to_set(person)
    add_to_queue = delegate("queue", "append")

    # def clear(self):
    #     self.queue.clear()
    clear = delegate("queue", "clear")
