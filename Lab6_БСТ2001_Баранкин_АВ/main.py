# Implementation of Johnson's algorithm

import time
from collections import defaultdict
import networkx as nx
from matplotlib import pyplot as plt

MAX_INT = float('Inf')


# Returns the vertex with minimum distance from the source
def min_distance(dist, visited):
    (minimum, min_vertex) = (MAX_INT, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and not visited[vertex]:
            (minimum, min_vertex) = (dist[vertex], vertex)

    return min_vertex


# Dijkstra Algorithm for Modified Graph (removing negative weights)
def Dijkstra(graph, modified_graph, src):
    # Number of vertices in the graph
    num_vertices = len(graph)

    # Dictionary to check if given vertex is already included in the shortest path tree
    spt_set = defaultdict(lambda: False)

    # Shortest distance of all vertices from the source
    dist = [MAX_INT] * num_vertices

    dist[src] = 0

    for count in range(num_vertices):

        # The current vertex which is at min Distance from the source and not yet included in the shortest path tree
        cur_vertex = min_distance(dist, spt_set)
        spt_set[cur_vertex] = True

        for vertex in range(num_vertices):
            if not spt_set[vertex] and dist[vertex] > (dist[cur_vertex] + modified_graph[cur_vertex][vertex]) and \
                    graph[cur_vertex][vertex] != 0:
                dist[vertex] = dist[cur_vertex] + modified_graph[cur_vertex][vertex]

    # Print the Shortest distance from the source
    for vertex in range(num_vertices):
        print('Vertex ' + str(vertex) + ': ' + str(dist[vertex]))


# Function to calculate the shortest distances from source to all other vertices using Bellman-Ford algorithm
def Bellman_Ford(edges, num_vertices):
    # Add a source s and calculate its min distance from every other node
    dist = [MAX_INT] * (num_vertices + 1)
    dist[num_vertices] = 0

    for i in range(num_vertices):
        edges.append([num_vertices, i, 0])

    for i in range(num_vertices):
        for (src, des, weight) in edges:
            if ((dist[src] != MAX_INT) and
                    (dist[src] + weight < dist[des])):
                dist[des] = dist[src] + weight

    # Don't send the value for the source added
    return dist[0:num_vertices]


# Function to implement Johnson Algorithm
def Johnson_Algorithm(graph):
    edges = []

    # Create a list of edges for Bellman-Ford Algorithm
    for i in range(len(graph)):
        for j in range(len(graph[i])):

            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])

    # Weights used to modify the original weights
    modify_weights = Bellman_Ford(edges, len(graph))

    modified_graph = [[0 for _ in range(len(graph))] for _ in
                      range(len(graph))]

    # Modify the weights to get rid of negative weights
    for i in range(len(graph)):
        for j in range(len(graph[i])):

            if graph[i][j] != 0:
                modified_graph[i][j] = (graph[i][j] +
                                        modify_weights[i] - modify_weights[j])

    print('Modified Graph: ' + str(modified_graph))

    # Run Dijkstra for every vertex as source one by one
    for src in range(len(graph)):
        print('\nShortest Distance with vertex ' +
              str(src) + ' as the source:\n')
        Dijkstra(graph, modified_graph, src)


# Create matrix
def make_matrix(m: int, n: int) -> list[list[int]]:
    return [[0 for _ in range(m)] for _ in range(n)]


# Main function
def main():
    start_time = time.time()

    # Create graph
    G: nx.DiGraph = nx.read_weighted_edgelist('graph.txt', create_using=nx.DiGraph)
    matrix = make_matrix(len(G.nodes), len(G.nodes))

    for (u, v, wt) in G.edges.data('weight'):
        matrix[int(u)][int(v)] = float(wt)

    print(matrix)

    Johnson_Algorithm(matrix)

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    print(f"{time.time() - start_time} sec.")
    plt.show()


# Driver Code
main()
