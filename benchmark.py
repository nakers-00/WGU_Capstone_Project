import Functions
from Hashtable import HashTable
from Package import Package
from Route import Route

package_data = Functions.read_package_csv('package.csv')
address_data = Functions.read_address_csv('addresses.csv')
distance_data = Functions.read_distance_csv('distances.csv')

# create inventory list based on the package data
inventory_list = []
for pack in package_data:
    p_num = int(pack[0])
    inventory_list.append(p_num)

# Information used for the benchmark route
benchmark_delivery_route = Route(inventory_list, 0.0,
                                 '4001 South 700 East')

benchmark_hash_table = HashTable()

# list to hold the benchmark route
benchmark_route = [0]


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


def calculate_benchmark(route, hash_table, distance_info):
    while len(route.not_delivered) > 0:
        package_delivered_id = route.not_delivered[0]
        package = hash_table.lookup(package_delivered_id)
        delivery_address = package.address

        distance = distance_between(route.current_address, delivery_address, distance_info)
        route.distance_traveled += distance
        route.not_delivered.remove(package_delivered_id)
        route.current_address = delivery_address
        benchmark_route.append(package_delivered_id)
        route.distance_list.append(round(route.distance_traveled, 1))

    distance_to_hub = distance_between(route.current_address, '4001 South 700 East', distance_info)
    route.distance_traveled += distance_to_hub
    route.current_address = '4001 South 700 East'
    route.distance_list.append(round(route.distance_traveled, 1))
    benchmark_route.append(0)


load_package_data(benchmark_hash_table, package_data)

calculate_benchmark(benchmark_delivery_route, benchmark_hash_table, distance_data)

print(benchmark_route)
print(benchmark_delivery_route.distance_traveled)