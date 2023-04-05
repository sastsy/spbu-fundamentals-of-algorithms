from typing import Any

import matplotlib.pyplot as plt
import networkx as nx

from queue import PriorityQueue

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set()

    mst_set.add(start_node)
    rest_set.remove(start_node)

    pqueue = PriorityQueue()

    for neighbor in G.neighbors(start_node):
        edge_data = G.get_edge_data(start_node, neighbor)
        edge_weight = edge_data["weight"]
        pqueue.put((edge_weight, (start_node, neighbor)))

    while len(mst_set) < len(G.nodes()):
        _, edge = pqueue.get(pqueue)

        if edge[0] not in mst_set:
            new_node = edge[0]
        elif edge[1] not in mst_set:
            new_node = edge[1]
        else:
            continue

        for neighbor in G.neighbors(new_node):
            edge_data = G.get_edge_data(new_node, neighbor)
            edge_weight = edge_data["weight"]
            pqueue.put((edge_weight, (new_node, neighbor)))

        mst_edges.add(tuple(sorted(edge)))
        mst_set.add(new_node)

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("spbu-fundamentals-of-algorithms/practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
