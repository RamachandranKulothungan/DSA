"""
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count_map_1 = {}
        for c in s1:
            count_map_1[c] = count_map_1.get(c, 0) + 1
        count_map_2 = {}
        for i in range(len(s1)):
            if s2[i] in count_map_1:
                count_map_2[s2[i]] = count_map_2.get(s2[i], 0) + 1
        l = 0
        r = len(s1) - 1
        while True:
            if count_map_1 == count_map_2:
                return True
            if r == len(s2) - 1:
                return False
            r = r + 1
            if s2[r] in count_map_1:
                count_map_2[s2[r]] = count_map_2.get(s2[r], 0) + 1
            if s2[l] in count_map_1:
                count_map_2[s2[l]] = count_map_2[s2[l]] - 1
            l = l + 1
