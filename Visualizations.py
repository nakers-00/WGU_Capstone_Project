import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def line_graph(x_axis):
    x = x_axis
    y = []
    for i in range(0, len(x)):
        y.append(i)

    plt.plot(x, y, marker='o')
    plt.xlabel('Distance(mi)')
    plt.ylabel('Stop Number')
    plt.title('Delivery Route')

    plt.xticks(np.arange(min(x), max(x) + 1, 5))
    plt.yticks(np.arange(min(y), max(y) + 1, 5))

    plt.show()


# xtest = [0.0, 2.0, 4.0, 4.0, 4.0, 7.0]
# line_graph(xtest)

def directed_graph(nodes, edges):
    nodes = nodes
    edges = edges

    plt.figure(figsize=(10, 8))
    G = nx.DiGraph()

    G.add_nodes_from(nodes)

    G.add_edges_from(edges)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', font_weight='bold', arrowsize=5)

    plt.show()


route = [0, 14, 15, 16, 34, 25, 26, 22, 24, 20, 21, 19, 12, 36, 6, 17, 31, 32, 4, 40, 28, 1, 2, 33, 7, 29, 10, 5, 9, 37,
         38, 3, 8, 30, 13, 39, 27, 35, 18, 23, 11, 0]

node_list = route

edge_list = []
for i in range(0, len(route) - 1):
    from_node = route[i]
    to_node = route[i + 1]

    edge = (from_node, to_node)
    edge_list.append(edge)

# directed_graph(node_list, edge_list)

package_data = [['1', '195 W Oakland Ave'], ['2', '2530 S 500 E'], ['3', '233 Canyon Rd'], ['4', '380 W 2880 S'],
                ['5', '410 S State St'], ['6', '3060 Lester St'], ['7', '1330 2100 S'], ['8', '300 State St'],
                ['9', '410 S State St'], ['10', '600 E 900 South'], ['11', '2600 Taylorsville Blvd'],
                ['12', '3575 W Valley Central Station bus Loop'], ['13', '2010 W 500 S'], ['14', '4300 S 1300 E'],
                ['15', '4580 S 2300 E'], ['16', '4580 S 2300 E'], ['17', '3148 S 1100 W'], ['18', '1488 4800 S'],
                ['19', '177 W Price Ave'], ['20', '3595 Main St'], ['21', '3595 Main St'],
                ['22', '6351 South 900 East'], ['23', '5100 South 2700 West'], ['24', '5025 State St'],
                ['25', '5383 S 900 East #104'], ['26', '5383 S 900 East #104'], ['27', '1060 Dalton Ave S'],
                ['28', '2835 Main St'], ['29', '1330 2100 S'], ['30', '300 State St'], ['31', '3365 S 900 W'],
                ['32', '3365 S 900 W'], ['33', '2530 S 500 E'], ['34', '4580 S 2300 E'], ['35', '1060 Dalton Ave S'],
                ['36', '2300 Parkway Blvd'], ['37', '410 S State St'], ['38', '410 S State St'], ['39', '2010 W 500 S'],
                ['40', '380 W 2880 S']]

address_data = [['0', 'Western Governors University', '4001 South 700 East'],
                ['1', 'International Peace Gardens', '1060 Dalton Ave S'], ['2', 'Sugar House Park', '1330 2100 S'],
                ['3', 'Taylorsville-Bennion Heritage City Gov Off', '1488 4800 S'],
                ['4', 'Salt Lake City Division of Health Services ', '177 W Price Ave'],
                ['5', 'South Salt Lake Public Works', '195 W Oakland Ave'],
                ['6', 'Salt Lake City Streets and Sanitation', '2010 W 500 S'],
                ['7', 'Deker Lake', '2300 Parkway Blvd'], ['8', 'Salt Lake City Ottinger Hall', '233 Canyon Rd'],
                ['9', 'Columbus Library', '2530 S 500 E'], ['10', 'Taylorsville City Hall', '2600 Taylorsville Blvd'],
                ['11', 'South Salt Lake Police', '2835 Main St'], ['12', 'Council Hall', '300 State St'],
                ['13', 'Redwood Park', '3060 Lester St'], ['14', 'Salt Lake County Mental Health', '3148 S 1100 W'],
                ['15', 'Salt Lake County/United Police Dept', '3365 S 900 W'],
                ['16', 'West Valley Prosecutor', '3575 W Valley Central Station bus Loop'],
                ['17', 'Housing Auth. of Salt Lake County', '3595 Main St'],
                ['18', 'Utah DMV Administrative Office', '380 W 2880 S'],
                ['19', 'Third District Juvenile Court', '410 S State St'],
                ['20', 'Cottonwood Regional Softball Complex', '4300 S 1300 E'],
                ['21', 'Holiday City Office', '4580 S 2300 E'], ['22', 'Murray City Museum', '5025 State St'],
                ['23', 'Valley Regional Softball Complex', '5100 South 2700 West'],
                ['24', 'City Center of Rock Springs', '5383 S 900 East #104'],
                ['25', 'Rice Terrace Pavilion Park', '600 E 900 South'],
                ['26', 'Wheeler Historic Farm ', '6351 South 900 East']]


def bar_graph(address_info, package_info):
    address_list = []
    num_packages = []

    for location in address_info:
        address_list.append(location[2])

    for address in address_list:
        count = 0
        for p in package_info:
            delivery_address = p[1]
            if delivery_address == address:
                count += 1
        num_packages.append(count)


    addresses = address_list
    packages = num_packages

    plt.figure(figsize=(10,8))
    plt.bar(addresses, packages)
    plt.xticks(rotation=90, ha='center')

    plt.xlabel('Delivery Address')
    plt.ylabel('Number of Packages')
    plt.title('Number of Packages per Delivery Address')

    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    plt.tight_layout()
    plt.show()


bar_graph(address_data, package_data)
