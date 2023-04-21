from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None  # type: ignore
    right: Node = None # type: ignore


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None # type: ignore

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self) -> list[Any]: # type: ignore

        if self.root is None:
            return []
        
        traversed_list = [[]]
        q = []
        next = []
        left_to_right = True

        q.append(self.root)

        while len(q) > 0:
            node = q.pop()
            if node.key:
                traversed_list[-1].append(node.key)
            if left_to_right:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            else:
                if node.right:
                    next.append(node.right)
                if node.left:
                    next.append(node.left)
            
            if len(q) == 0:
                left_to_right = not left_to_right
                q, next = next, q
                if len(q) != 0:
                    traversed_list.append([])

        return traversed_list


def build_tree(list_view: list[Any]) -> BinaryTree: # type: ignore
    bt = BinaryTree()

    if len(list_view) == 0:
        return bt

    bt.root = Node(list_view[0])

    q = [bt.root]
    i = 1
    while i < len(list_view):
        current_node = q.pop(0)
        if i < len(list_view):
            current_node.left = Node(list_view[i])
            q.append(current_node.left)
            i += 1
        if i < len(list_view):
            current_node.right = Node(list_view[i])
            q.append(current_node.right)
            i += 1

    return bt
    



if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        "spbu-fundamentals-of-algorithms/practicum_6/homework/binary_tree_zigzag_level_order_traversal_cases.yaml", "r"
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal()
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
        print(zz_traversal)
