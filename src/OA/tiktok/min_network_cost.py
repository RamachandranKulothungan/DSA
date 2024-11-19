"""
There are n data centres in a network. Each data centre has location (x_i, j_i). Connecting any two data centre 
costs: min(|x_i - x_j|, |y_i - y_j|). We need all data centres to be connected either directly or indirectly.
What is the minimum cost for creating this network?

Inputs:
x = [x_1, x_2, ..., x_n]
y = [y_1, y_2, ..., y_n]

Similar problem: https://leetcode.com/problems/min-cost-to-connect-all-points/description/
"""

class MyDict:
    def __init__(self):
        self.dict = {}
    
    def __getitem__(self, key):
        if key in self.dict:
            return self.dict[key]
        return None
    
    def __setitem__(self, key, value):
        self.dict[key] = value
    
    def __repr__(self):
        return f"{self.dict}"

class Solution:

    def __init__(self):
        self.parent = MyDict()
 
    def root(self, k):
        if self.parent[k] is None:
            return k
        self.parent[k] = self.root(self.parent[k])
        return self.parent[k]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                edges.append((i, j, abs(points[i][0] - points[j][0])+ abs(points[i][1] - points[j][1])))
        min_cost = 0
        sorted_edges = sorted(edges, key=lambda x: x[2])
        included_edges = []
        for edge in sorted_edges:
            parent_i = self.root(edge[0])
            parent_j = self.root(edge[1])
            if parent_i != parent_j:
                min_cost = min_cost + edge[2]
                self.parent[parent_i] = parent_j
                included_edges.append(edge)
        return min_cost

        