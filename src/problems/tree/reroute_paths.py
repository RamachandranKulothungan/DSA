"""
Reorder Routes to Make All Paths Lead to the City Zero
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
"""

# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/


class Solution:
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        outgoing_connections_map = {}
        incoming_connections_map = {}

        for conn in connections:
            outgoing_connections_map[conn[0]] = outgoing_connections_map.get(
                conn[0], []
            ) + [conn[1]]
            incoming_connections_map[conn[1]] = incoming_connections_map.get(
                conn[1], []
            ) + [conn[0]]
        # print(outgoing_connections_map)
        # print(incoming_connections_map)
        nodes = [(0, 0)]
        left = 0
        right = 1
        count = 0
        while left < right:
            # print(nodes)
            curr = nodes[left][0]
            prev = nodes[left][1]
            left = left + 1
            if outgoing_connections_map.get(curr):
                for invalid_node in outgoing_connections_map[curr]:
                    if invalid_node == prev:
                        continue
                    # print(f'add and reverse invalid connecting node {curr} to {invalid_node}')
                    nodes.append((invalid_node, curr))
                    count += 1
                    right += 1
            if incoming_connections_map.get(curr):
                for valid_node in incoming_connections_map[curr]:
                    if valid_node == prev:
                        continue
                    # print(f'add valid connecting node {valid_node} to {curr}')
                    nodes.append((valid_node, curr))
                    right += 1

            # Takes more time due to extra empty nodes
            # for i in range(n):
            #     if i == prev:
            #         continue
            #     if connection_matrix[i][curr] == 1:
            #         nodes.append((i, curr))
            #         right+=1
            #         print(f'add valid connecting node {i} to {curr}')
            #     if connection_matrix[curr][i] == 1:
            #         print(f'add and reverse invalid connecting node {curr} to {i}')
            #         nodes.append((i, curr))
            #         count += 1
            #         right+=1
        return count
