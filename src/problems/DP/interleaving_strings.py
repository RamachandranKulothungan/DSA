"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2. 
An interleaving of two strings a and b is a configuration where a and b are divided into n 
and m substrings respectively, such that: a = a1 + a2 + ... + an, b = b1 + b2 + ... + bm and 
|n - m| ≤ 1. The interleaving is a1 + b1 + a2 + b2 + a3 + b3 + ... or b1 + a1 + b2 + a2 + b3 + a3 + .... 
Note: ai + bj is the concatenation of strings ai and bj . Describe a Dynamic Programming algorithm (Define sub-problems, 
establish base case and recurrence relations between sub-problems, write the dynamic programming algorithm pseudo-code.) 
for solving this problem in O(|s1| · |s2|)-time. For convenience, you only need to output the solution “true” or “false”. 
For example, Input: s1 = “aabcc”, s2= “dbbca”, s3 = “aadbbcbcac” Output: “true”. Explanation: One way to obtain s3 is: 
Split s1 into s1 = “aa” + “bc” + “c”, and s2 into s2 = “dbbc” + “a”. 
Interleaving the two splits, we get “aa” + “dbbc” + “bc” + “a” + “c” = “aadbbcbcac”. Since s3 can be obtained by interleaving 
s1 and s2, we return “true”.
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                if j > 0 and s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        return dp[len(s1)][len(s2)]

import heapq

heapq.hea