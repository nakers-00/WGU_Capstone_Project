# Course: C964 - Name: Noah Akers - Student ID: 011359614
import Functions
from Hashtable import HashTable
from Package import Package
from Route import Route
from builtins import ValueError
from Visualizations import bar_graph, line_graph, directed_graph

package_data = Functions.read_package_csv('package.csv')
address_data = Functions.read_address_csv('addresses.csv')
distance_data = Functions.read_distance_csv('distances.csv')

# create inventory list based on the package data
inventory_list = []
for pack in package_data:
    p_num = int(pack[0])
    inventory_list.append(p_num)

delivery_route = Route(inventory_list, 0.0,
                       '4001 South 700 East')

package_hash_table = HashTable()
final_route = [0]


# This method takes a hash table and package information as input and loops through the package information array to
# create package objects and insert them into the hash table
def load_package_data(hash_table, package_info):
    for p in package_info:
        p_id = int(p[0])
        p_address = p[1]

        package = Package(p_id, p_address)

        hash_table.insert(p_id, package)


# The following methods will be involved in the actual implementation of the nearest neighbor algorithm
# This method returns the index of an address in the array input as address_info
def find_address_index(address, address_info):
    # O(n) time complexity due to the for loop
    for item in address_info:
        if item[2] == address:
            return item[0]


# This method finds the distance between two given addresses.
def distance_between(address1, address2, distance_info):
    # Get the index of each address in the address_data array
    address1_index = int(find_address_index(address1, address_data))
    address2_index = int(find_address_index(address2, address_data))

    # The indices from address_data correspond to the indices in distance_data, so simply plug in those indices to
    # find the distance between the two addresses
    distance = distance_info[address1_index][address2_index]
    distance = float(distance)
    return distance


# This method takes in an address and compares it with the delivery address of each package in the list.
def min_distance_from(from_address, route_not_delivered, hash_table):
    # min_distance set to 1000.0 to ensure that the first address compared will always be closer
    min_distance = 1000.0
    nearest_package_address = None
    package_id_to_remove = None

    # Loop through the inventory and find the distance between each package address and the from_address.
    # Compare that distance with the current min_distance to find the nearest neighbor. Return the delivery address
    # of that nearest neighbor package.
    for package_id in route_not_delivered:
        package = hash_table.lookup(package_id)
        # Updates min_distance if a package is found to have a closer delivery address to from_address
        distance = distance_between(from_address, package.address, distance_data)
        if distance < min_distance:
            package_id_to_remove = package_id
            nearest_package_address = package.address
            min_distance = distance

    return nearest_package_address, package_id_to_remove


# This method uses the methods and objects defined above to determine an efficient order to deliver the packages.
def calculate_route(route, hash_table, distance_info):

    while len(route.not_delivered) > 0:

        delivery_address, package_delivered_id = min_distance_from(route.current_address, route.not_delivered,
                                                                   hash_table)
        package_delivered_id = int(package_delivered_id)

        distance = distance_between(route.current_address, delivery_address, distance_info)
        # Increment the distance traveled by the route
        route.distance_traveled += distance
        # Remove the delivered package from the route.not_delivered list
        route.not_delivered.remove(package_delivered_id)
        # Change the route current address to the address of the most recently delivered package
        route.current_address = delivery_address

        route.distance_list.append(round(route.distance_traveled, 1))
        # Add stop to final_route
        final_route.append(package_delivered_id)

    # The address of the hub is input directly as the hub address.
    distance_to_hub = distance_between(route.current_address, '4001 South 700 East', distance_info)
    route.distance_traveled += distance_to_hub
    route.current_address = '4001 South 700 East'
    route.distance_list.append(round(route.distance_traveled, 1))
    final_route.append(0)


# Loads the package_hash_table with package objects
load_package_data(package_hash_table, package_data)

# Calculates delivery route
calculate_route(delivery_route, package_hash_table, distance_data)

# Formats string for route output
route_string = f""""""
for delivery in final_route:
    route_string += f"{delivery} "


# User command line interface
class Main:
    # While loop used so that the program will continue to ask for input until the user decides to exit the program.
    while True:
        # This try-except block encompasses the interface code and will close the program if user input causes a
        # Value Error
        try:
            # Gets input from user
            user_input = input("Hello! Would you like to see your delivery route?(Y/N) - "
                               "type 'exit' to close program: ")
            # Checks if the user entered 'Exit'. If so, the program is terminated
            if user_input.lower() == 'exit':
                print("Goodbye!")
                exit()
            elif user_input.upper() == "Y":
                print(f"""\nBelow is the order in which to deliver the packages ('0' represents the shipping hub):
{route_string}""")
                print(f"""Route Distance: {round(delivery_route.distance_traveled, 1)} miles\n""")
            elif user_input.upper() == "N":
                print("Okay, skipping delivery route.")
            else:
                print("Invalid input. Please ensure that you are following the prompts. Closing Program.")
                exit()

            bar_graph_question = input(
                "Would you like to view a bar graph showing how many packages are delivered to each "
                "address?(Y/N) - type 'exit' to close program: ")
            if bar_graph_question.lower() == 'exit':
                print("Goodbye!")
                exit()
            elif bar_graph_question.upper() == "Y":
                bar_graph(address_data, package_data)
            elif bar_graph_question.upper() == "N":
                print("Okay, skipping bar graph.\n")
            else:
                print("Invalid input. Please ensure that you are following the prompts. Closing Program.")
                exit()

            line_graph_question = input(
                "Would you like to view a line graph representing the distance of the route?(Y/N) - "
                "type 'exit' to close program: ")
            if line_graph_question.lower() == 'exit':
                print("Goodbye!")
                exit()
            elif line_graph_question.upper() == "Y":
                line_graph(delivery_route.distance_list)
            elif line_graph_question.upper() == "N":
                print("Okay, skipping line graph.\n")
            else:
                print("Invalid input. Please ensure that you are following the prompts. Closing Program.")
                exit()

            directed_graph_question = input("Would you like to view a directed graph representing order of package "
                                            "deliveries?(Y/N) - type 'exit' to close program: ")
            if directed_graph_question.lower() == 'exit':
                print("Goodbye!")
                exit()
            elif directed_graph_question.upper() == "Y":
                directed_graph(final_route)
                exit()
            elif directed_graph_question.upper() == "N":
                print("Okay, skipping directed graph.\n")
                exit()
            else:
                print("Invalid input. Please ensure that you are following the prompts. Closing Program.")
                exit()

        except ValueError:
            print("Invalid input. Please ensure that you are following the prompts. Closing Program.")
            exit()
