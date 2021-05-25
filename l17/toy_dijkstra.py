import networkx as nx  # Optional
import numpy as np  # Optional


def toy_dijkstra(graph, source):

    unexplored = set(graph)  # unexplored nodes
    D = dict.fromkeys(graph, np.inf)
    p = dict.fromkeys(graph)
    update_nodes(graph, unexplored, D, p, source, 0)

    while unexplored:
        node, cost = find_minimum(unexplored, D)
        update_nodes(graph, unexplored, D, p, node, cost)

    return (D, p)


def update_nodes(graph, unexplored, D, p, node, cost):

    unexplored.remove(node)
    D[node] = cost

    unexplored_neighbors = unexplored.intersection(graph[node])
    for neighbor in unexplored_neighbors:
        temp = cost + graph[neighbor][node]['cost']
        if temp < D[neighbor]:
            D[neighbor] = temp
            p[neighbor] = node


def find_minimum(unexplored, D):
    minimum = np.inf
    for node in unexplored:
        if D[node] < minimum:
            node_min = node
            minimum = D[node]
    return (node_min, minimum)
