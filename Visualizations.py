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

directed_graph(node_list, edge_list)
