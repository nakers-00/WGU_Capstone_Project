# Course: C950 - Name: Noah Akers - Student ID: 011359614
from datetime import timedelta
import Functions
from Hashtable import HashTable
from Package import Package
from Route import Route
from builtins import ValueError
from Visualizations import line_graph

package_data = Functions.read_package_csv('package.csv')
address_data = Functions.read_address_csv('addresses.csv')
distance_data = Functions.read_distance_csv('distances.csv')

# create inventory list based on the package data
inventory_list = []
for package in package_data:
    p_num = int(package[0])
    inventory_list.append(p_num)

delivery_route = Route(inventory_list, 0.0,
                       '4001 South 700 East')

package_hash_table = HashTable()
final_route = [0]


# This method takes a hash table and package information as input and loops through the package information array to
# create package objects and insert them into the hash table
# O(n^2) time complexity because the for loop calls hash_table.insert(), which is a method of the HashTable class and
# contains a for-loop
# Space complexity O(1)
def load_package_data(hash_table, package_info):
    # O(n) time complexity due to the for loop
    for p in package_info:
        p_id = int(p[0])
        p_address = p[1]

        package = Package(p_id, p_address)

        hash_table.insert(p_id, package)


# The following methods will be involved in the actual implementation of the nearest neighbor algorithm
# This method returns the index of an address in the array input as address_info
# O(n) due to the for-loop
# O(1) space complexity
def find_address_index(address, address_info):
    # O(n) time complexity due to the for loop
    for item in address_info:
        if item[2] == address:
            return item[0]


# This method finds the distance between two given addresses. This method has a time complexity of O(n) because it
# calls find_address_index which has a for-loop and is therefore O(n)
# Space complexity is O(1)
def distance_between(address1, address2, distance_info):
    # Get the index of each address in the address_data array
    address1_index = int(find_address_index(address1, address_data))
    address2_index = int(find_address_index(address2, address_data))

    # The indices from address_data correspond to the indices in distance_data, so simply plug in those indices to
    # find the distance between the two addresses
    distance = distance_info[address1_index][address2_index]
    distance = float(distance)
    return distance


# This method takes in an address and compares it with the delivery address of each package in the list of
# undelivered packages on the truck. It then returns the address and package ID of the package with the nearest delivery
# address to the current address (from_address). truck_not_delivered will be truck.not_delivered, so it will be a list
# of package IDs which correspond to package objects stored in the hash table.
# It has O(n^2) time complexity due to a for loop which calls the .lookup() method and distance_between() method.
# The .lookup() and distance_between methods both have O(n) time complexity and they are nested at the same level within
# the outer for-loop; therefore, the time complexity is O(n * 2n) which would simply be O(n^2).
# O(1) space complexity
def min_distance_from(from_address, route_not_delivered, hash_table):
    # min_distance set to 1000.0 to ensure that the first address compared will always be closer
    min_distance = 1000.0
    nearest_package_address = None
    package_id_to_remove = None

    # Loop through the truck inventory and find the distance between each package address and the from_address.
    # Compare that distance with the current min_distance to find the nearest neighbor. Return the delivery address
    # of that nearest neighbor package.
    for package_id in route_not_delivered:
        # Finds the package object stored in the hash table corresponding to package ID in the truck inventory
        package = hash_table.lookup(package_id)
        # Updates min_distance if a package is found to have a closer delivery address to from_address
        distance = distance_between(from_address, package.address, distance_data)
        if distance < min_distance:
            package_id_to_remove = package_id
            nearest_package_address = package.address
            min_distance = distance

    return nearest_package_address, package_id_to_remove


# This method uses the methods and objects defined above to determine an efficient order to deliver the packages.
# The time complexity is O(n^3) due to a while-loop which calls the .lookup() (O(n)), min_distance_from() (O(n^2)), and
# distance_between() (O(n)) methods. Due to the time complexities and organization of these methods, the time complexity
# of deliver_packages() simplifies to O(n^3).
# O(1) space complexity
def deliver_packages(route, hash_table, distance_info):
    # O(n) time complexity from while loop
    while len(route.not_delivered) > 0:
        # O(n^2) time complexity
        delivery_address, package_delivered_id = min_distance_from(route.current_address, route.not_delivered,
                                                                   hash_table)
        package_delivered_id = int(package_delivered_id)
        # O(n)
        distance = distance_between(route.current_address, delivery_address, distance_info)
        # Increment the distance traveled by the route
        route.distance_traveled += distance
        # Remove the delivered package from the route.not_delivered list
        route.not_delivered.remove(package_delivered_id)
        # Change the route current address to the address of the most recently delivered package
        route.current_address = delivery_address

        route.distance_list.append(round(route.distance_traveled, 0))
        # Add stop to final_route
        final_route.append(package_delivered_id)
    # O(n)
    # The address of the hub is input directly as the hub address. If this program is being used in another city/state,
    # the hub address should be updated here.
    distance_to_hub = distance_between(route.current_address, '4001 South 700 East', distance_info)
    route.distance_traveled += distance_to_hub
    route.current_address = '4001 South 700 East'
    route.distance_list.append(round(route.distance_traveled, 0))
    final_route.append(0)


# Loads the package_hash_table created on line 25 with package objects
load_package_data(package_hash_table, package_data)

# Delivers packages using the method defined on line 96-121
deliver_packages(delivery_route, package_hash_table, distance_data)

print(package_data)
print(final_route)
print(delivery_route.distance_list)

# line_graph(delivery_route.distance_list)

# User command line interface
# Overall time complexity is O(n^3) due to the while-loop containing nested for-loops. Although there are multiple
# for-loops nested within the while-loop, all their complexities will not multiply duo to their organization.
# Therefore, the simplified time complexity is O(n^3).
# Space complexity is O(1)
# class Main:
#     # While loop used so that the program will continue to ask for input until the user decides to exit the program.
#     while True:
#         # This try-except block encompasses the interface code and will close the program if user input causes a
#         # Value Error
#         try:
#             # Gets input from user
#             user_input = input("Would you like to see your delivery route?(Y/N) - "
#                                "type 'exit' to close program: ")
#             # Checks if the user entered 'Exit'. If so, the program is terminated
#             if user_input.lower() == 'exit':
#                 print("Goodbye!")
#                 exit()
#             elif user_input == "Y":
#                 print(final_route)
#
#             # user_input = input("If you would like to view a single package, please enter the package ID number. Type "
#             #                    "'All' to view all packages - type 'exit to close program: ")
#             # # Checks if the user entered 'Exit'. If so, the program is terminated
#             # if user_input.lower() == 'exit':
#             #     print("Goodbye!")
#             #     exit()
#
#         except ValueError:
#             print("Invalid input. Please ensure that you are entering valid inputs into each field. Closing Program.")
#             exit()
