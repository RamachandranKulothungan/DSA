"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [1,1,3,3]

Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        if len(nums) == 2:
            return dp[-1]
        for i in range(2, len(nums)):
            dp.append(max(dp[i-1], dp[i-2]+nums[i]))
        print(dp)
        return dp[-1]