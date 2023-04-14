from typing import Any

import matplotlib.pyplot as plt
import networkx as nx

import numpy as np

from queue import PriorityQueue

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set()

    while rest_set:
        for node in G.nodes():
            minimum_edge = np.inf
            if node not in mst_set:
                
                for neighbor in G.neighbors(node):
                    if G[node][neighbor]['weight'] < minimum_edge and neighbor not in mst_set:
                        minimum_edge = G[node][neighbor]['weight']
                        minimum_node = neighbor
                

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("spbu-fundamentals-of-algorithms/practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
