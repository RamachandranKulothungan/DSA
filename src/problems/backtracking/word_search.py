"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        size = (len(board), len(board[0]))
        visited = [[False for x in range(size[1])] for x in range(size[0])]

        def rec_exist(start, i, j):
            if len(word) == start:
                return True
            if i < 0 or j < 0 or i == size[0] or j == size[1]:
                return False
            if word[start] != board[i][j]:
                return False
            if visited[i][j]:
                return False
            visited[i][j] = True
            possible_next_terms = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
            found = False
            for possible_term in possible_next_terms:
                found = rec_exist(start + 1, *possible_term)
                if found:
                    break
            visited[i][j] = False
            return found

        for i in range(size[0]):
            for j in range(size[1]):
                rec_exists = rec_exist(0, i, j)
                if rec_exists:
                    return True
        return False
