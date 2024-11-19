"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def __init__(self):
        self.node_map = {}
        self.visited = set()

    def dfs(self, node):
        if node.val not in self.node_map:
            self.node_map[node.val] = Node(node.val)
        self.visited.add(node.val)
        for neighbor in node.neighbors:
            if neighbor.val in self.visited:
                self.node_map[node.val].neighbors.append(self.node_map[neighbor.val])
                continue
            new_neighbor = self.dfs(neighbor)
            self.node_map[node.val].neighbors.append(new_neighbor)
        return self.node_map[node.val]

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        self.dfs(node)
        return self.node_map[1]

        