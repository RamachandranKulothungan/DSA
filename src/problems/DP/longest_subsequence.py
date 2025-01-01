"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Using memoisation and recursion
        # dp = {}
        # def rec_lcs(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
        #     if f"{i}, {j}" in dp.keys():
        #         return dp[f"{i}, {j}"]
        #     if text1[i] == text2[j]:
        #         dp[f"{i}, {j}"] = rec_lcs(i+1, j+1) + 1
        #         return dp[f"{i}, {j}"]
        #     skip_i = rec_lcs(i+1, j)
        #     skip_j = rec_lcs(i, j+1)
        #     dp[f"{i}, {j}"] = max(skip_i, skip_j)
        #     return dp[f"{i}, {j}"]
        # return rec_lcs(0,0)
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        lcs = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                    lcs = max(lcs, dp[j][i])
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
        return lcs
