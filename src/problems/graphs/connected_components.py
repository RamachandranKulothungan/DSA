"""
Number of Connected Components in an Undirected Graph
There is an undirected graph with n nodes. There is also an edges array, 
where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
"""


class Solution:
    def countComponents(self, n: int, edges) -> int:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for edge in edges:
            adj_list[edge[0]] = adj_list[edge[0]] + [edge[1]]
            adj_list[edge[1]] = adj_list[edge[1]] + [edge[0]]
        count = 0
        visited = {}
        for i in range(n):
            visited[i] = 0
        # print(adj_list)
        # print(visited)

        def dfs(node):
            visited[node] = 1
            for adj in adj_list[node]:
                if visited[adj] == 0:
                    dfs(adj)

        for i in range(n):
            if visited[i] == 0:
                count += 1
                dfs(i)
        return count
