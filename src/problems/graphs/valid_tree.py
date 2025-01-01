"""
Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.
Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
"""


class Solution:
    def validTree(self, n: int, edges) -> bool:
        adjacency_list = {}
        for i in range(n):
            adjacency_list[i] = []
        for edge in edges:
            adjacency_list[edge[0]] = adjacency_list.get(edge[0], []) + [edge[1]]
            adjacency_list[edge[1]] = adjacency_list.get(edge[1], []) + [edge[0]]

        def isValidTree():
            if len(adjacency_list) == 1:
                return list(adjacency_list.values()) == [[]]
            leaf_nodes = []
            for node in adjacency_list:
                if not adjacency_list[node]:
                    return False
                if len(adjacency_list[node]) == 1:
                    leaf_nodes.append(node)
            if not leaf_nodes:
                return False
            if len(leaf_nodes) == len(adjacency_list) and len(adjacency_list) == 2:
                return True
            for leaf_node in leaf_nodes:
                if not adjacency_list[leaf_node]:
                    return False
                for conn_node in adjacency_list[leaf_node]:
                    adjacency_list[conn_node].remove(leaf_node)
                del adjacency_list[leaf_node]
            return isValidTree()

        return isValidTree()
