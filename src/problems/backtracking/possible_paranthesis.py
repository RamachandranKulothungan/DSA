"""
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solution = []
        def check_possible(curr_left, curr_right, curr_string):
            if curr_left < curr_right:
                return
            if curr_left > n or curr_right > n:
                return
            if curr_left == n and curr_right == n:
                solution.append(curr_string)
                return
            check_possible(curr_left+1, curr_right, curr_string+"(")
            check_possible(curr_left, curr_right + 1, curr_string+")")
        check_possible(0,0,"")
        return solution