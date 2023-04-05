import queue
from typing import Any
import networkx as nx
from src.plotting import plot_graph
from collections import deque


def visit(node: Any):
    print(f"Wow, it is {node} right here!")


def dfs_iterative(G: nx.Graph, node: Any, visited: dict) -> list:
    stack = []
    stack.append(node)
    path = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            path.append(node)
            for neighbour in G.neighbors(node):
                stack.append(neighbour)
    return path

        

def topological_sort(G: nx.DiGraph, node: Any) -> list:
    visited = {n: False for n in G}
    result = [n for n in G.nodes if len(list(G.predecessors(n))) == 0]

    for node in G.nodes:
        result += dfs_iterative(G, node, visited)
    print(list(dict.fromkeys(result)))


if __name__ == "__main__":
    # Load and plot the graph
    G = nx.read_edgelist("spbu-fundamentals-of-algorithms/practicum_2/homework/graph_2.edgelist", create_using=nx.DiGraph)
    # plot_graph(G)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="0", visited={n: False for n in G})
    print()

    G = nx.read_edgelist(
        "spbu-fundamentals-of-algorithms/practicum_2/homework/graph_2.edgelist", create_using=nx.DiGraph
    )
    plot_graph(G)
    print("Topological sort")
    print("-" * 32)
    topological_sort(G, node="0")
