import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def line_graph(distances):
    y = distances
    x = []
    for i in range(0, len(y)):
        x.append(i)

    plt.plot(x, y, marker='o')
    plt.xlabel('Number of Deliveries')
    plt.ylabel('Distance(mi)')
    plt.title('Delivery Route Distance')

    plt.xticks(np.arange(min(x), max(x) + 1, 5))
    plt.yticks(np.arange(min(y), max(y) + 1, 5))

    plt.show()


def directed_graph(route):
    edge_list = []
    for i in range(0, len(route) - 1):
        from_node = route[i]
        to_node = route[i + 1]

        edge = (from_node, to_node)
        edge_list.append(edge)

    nodes = route
    edges = edge_list

    plt.figure(figsize=(10, 8))
    G = nx.DiGraph()

    G.add_nodes_from(nodes)

    G.add_edges_from(edges)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', font_weight='bold', arrowsize=10)

    plt.show()


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

    plt.figure(figsize=(10, 8))
    plt.bar(addresses, packages)
    plt.xticks(rotation=90, ha='center')

    plt.xlabel('Delivery Address')
    plt.ylabel('Number of Packages')
    plt.title('Number of Packages per Delivery Address')

    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    plt.tight_layout()
    plt.show()
