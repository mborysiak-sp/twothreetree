from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self) -> None:
        self.values = []
        self.parent: Optional[Node] = None
        self.children: dict[int, Node] = {}

    def insert(self, x: int) -> None:
        self.values.append(x)
        self.values.sort()

    def search(self, x: int) -> Node:
        if not self.children:
            return self
        children_sorted_list = sorted(self.children.items())
        for number, key, node in enumerate(children_sorted_list):
            # If x is smaller than specified key then return node assigned to that key
            if x < key:
                return node.search(x)
            # If x is larger than any other key (didn't return above for any node)
            # and it is the last node then return it
            return node.search(x)

    def attach_node(self, key: int, node: Node) -> None:
        self.children[key] = node
        self.balance()

    def balance(self):
        if not self.parent:
            parent = Node()
        else:
            parent = self.parent

        if len(self.values) == 4:
            other_node = Node()
            other_node.values.append(self.values[2:])
            self.values = self.values[:2]
            other_node.parent = parent
            self.parent.attach_node(other_node.values[-1], other_node)

        if len(self.children) == 4:
            other_node = Node()
            children_sorted_list = sorted(self.children.items())
            for number, key, node in enumerate(children_sorted_list):
                if number >= 2:
                    other_node.attach_node(key, node)
                    self.children.pop(key)
            other_node.parent = parent
            parent.attach_node(
                max(k for k, v in other_node.children.items()),
                other_node
            )


class TwoThreeTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None
        self.keys = []

    def insert(self, x: int) -> None:
        if x in self.keys:
            print(f'Value {x} is already in the tree')
            return None
        node_to_store_in = self.search(x)
        node_to_store_in.insert(x)
        self.keys.append(x)

    def search(self, x: int) -> Node:
        return self.root.search(x)
