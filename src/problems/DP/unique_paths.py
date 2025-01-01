"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            dp[-1][i] = 1
        for j in range(n):
            dp[j][-1] = 1
        # print(dp)
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                right = 0
                down = 0
                if i < m - 1:
                    right = dp[j][i + 1]
                if j < n - 1:
                    down = dp[j + 1][i]
                # print(i, j, right, down)
                dp[j][i] = down + right
        # print(dp)
        return dp[0][0]
