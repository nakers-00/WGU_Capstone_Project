# Create a package class with the necessary attributes
class Package:
    def __init__(self, package_id, delivery_address):
        self.id = package_id
        self.address = delivery_address

    def __str__(self):
        return "%s, %s" % (self.id, self.address)
