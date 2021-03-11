class Flight:
    def __init__(self, capacity):
        # function create a flight  by storing one input of an object in property called x
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_seat():
            return False
        self.passenger.append(name)
        return True

    def open_seat(self):
        return self.capacity - len(self.passenger)


flight = Flight(3)
people = ["Diana", "Harry", "Charles", "Elizabeth"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person } to the flight")
    else:
        print(f"No seat available to {person }")
