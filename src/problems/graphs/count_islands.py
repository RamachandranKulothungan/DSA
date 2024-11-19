"""
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

"""


class Solution:
    def numIslands(self, grid) -> int:
        x = len(grid)
        y = len(grid[0])
        visited = [[False for j in range(y)] for i in range(x)]
        islands = 0

        def dfs(i, j):
            visited[i][j] = True
            coordinates = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for neighbour in coordinates:
                if (
                    neighbour[0] < x
                    and neighbour[0] > -1
                    and neighbour[1] < y
                    and neighbour[1] > -1
                ):
                    if grid[neighbour[0]][neighbour[1]] == "1":
                        if not visited[neighbour[0]][neighbour[1]]:
                            print(f"visiting neighbour {neighbour}")
                            dfs(*neighbour)

        for i in range(x):
            for j in range(y):
                if not visited[i][j]:
                    if grid[i][j] == "1":
                        print(i, j)
                        dfs(i, j)
                        islands += 1
        return islands
