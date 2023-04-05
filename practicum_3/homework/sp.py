from typing import Any

import networkx as nx
from queue import PriorityQueue
import numpy as np

from src.plotting import plot_graph


def find_min_vertex(distance: dict[int], unvisited: list, min_vertex):
    for node in unvisited:
            if distance[min_vertex] > distance[node]:
                min_vertex = node
    return min_vertex


def find_min_distance(min_vertex, distance:dict, shortest_paths: list) -> list:
     for neighbor in G.neighbors(min_vertex):
            dst = G[min_vertex][neighbor]["weight"] + distance[min_vertex]
            if distance[neighbor] > dst:
                distance[neighbor] = dst
                shortest_paths[neighbor] = shortest_paths[min_vertex] + [neighbor]


def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = {}  # key = destination node, value = list of intermediate nodes
    unvisited = G.nodes()

    distance = {}
    distance[source_node] = 0
    for node in G.nodes():
        shortest_paths[node] = ['0']
        distance[node] = np.inf

    while unvisited:
        min_vertex = find_min_vertex(distance, unvisited, unvisited[0])
        find_min_distance(min_vertex, distance, shortest_paths)
        unvisited.remove(min_vertex)
    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("spbu-fundamentals-of-algorithms/practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
