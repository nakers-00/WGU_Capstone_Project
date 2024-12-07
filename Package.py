# Create a package class with the necessary attributes


class Package:
    def __init__(self, package_id, delivery_address):
        self.id = package_id
        self.address = delivery_address

    # # Check the status of package at the specified time
    # def package_status(self, time):
    #     if self.delivery_time < time:
    #         self.status = "Delivered"
    #     elif self.depart_time < time:
    #         self.status = "En Route"
    #     else:
    #         self.status = "At Hub"

    def __str__(self):
        return "%s, %s" % (self.id, self.address)
