from collections import deque

class BikeRentalSystem:
    def __init__(self):
        self.undo_stack = []  
        self.rental_queue = deque()  
        self.available_bikes = []  

    def add_bike(self, bike_id):
        self.available_bikes.append(bike_id)

    def schedule_rental(self, customer_id):
        if self.available_bikes:
            bike_id = self.available_bikes.pop(0)
            self.rental_queue.append((customer_id, bike_id))
            self.undo_stack.append(("schedule", customer_id, bike_id))
            return f"Rental scheduled for customer {customer_id} with bike {bike_id}"
        return "No bikes available"

    def complete_rental(self):
        if self.rental_queue:
            customer_id, bike_id = self.rental_queue.popleft()
            return f"Rental completed for customer {customer_id} with bike {bike_id}"
        return "No scheduled rentals"

    def undo_last_action(self):
        if self.undo_stack:
            action, customer_id, bike_id = self.undo_stack.pop()
            if action == "schedule":
                self.rental_queue = deque([r for r in self.rental_queue if r != (customer_id, bike_id)])
                self.available_bikes.append(bike_id)
                return f"Undone: Rental scheduling for customer {customer_id} with bike {bike_id}"
        return "Nothing to undo"


rental_system = BikeRentalSystem()

rental_system.add_bike("Bike1")
rental_system.add_bike("Bike2")


print(rental_system.schedule_rental("Customer1"))
print(rental_system.schedule_rental("Customer2"))


print(rental_system.complete_rental())


print(rental_system.undo_last_action())


print("Available bikes:", rental_system.available_bikes)
