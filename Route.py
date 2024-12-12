# Create a route class with the required attributes

class Route:
    def __init__(self, inventory, distance_traveled,
                 current_address):
        self.not_delivered = inventory
        self.distance_traveled = distance_traveled
        self.current_address = current_address
        self.distance_list = [0.0]

    def __str__(self):
        return "%s, %s, %s" % (
            self.not_delivered, self.distance_traveled, self.current_address)
