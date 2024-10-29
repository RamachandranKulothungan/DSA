"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

class Solution:
    def __init__(self):
        self.candidates = []
        self.len_candidates = 0

    def rec_combination_sum(self, i, target):
        if target==0:
            return [[]]
        if i == self.len_candidates:
            return []
        res = target
        total_sol = []
        curr = []
        while target>=0:
            poss_sol = self.rec_combination_sum(i+1, target)
            if poss_sol:
                for sol in poss_sol:
                    total_sol.append(sol + curr)
            curr.append(self.candidates[i])
            target = target - self.candidates[i]
        return total_sol
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.len_candidates = len(candidates)
        return self.rec_combination_sum(0, target)
        