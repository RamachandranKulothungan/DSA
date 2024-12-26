"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [3,4,3]

Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.
"""
class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0],max(nums[0], nums[1])]
        if len(nums) == 2:
            return dp[-1]
        dp_not_1 = [nums[1], max(nums[1], nums[2])]
        if len(nums)==3:
            return max(dp[-1], dp_not_1[-1])
        for i in range(2, len(nums)-1):
            dp.append(max(dp[i-1], dp[i-2]+nums[i]))
        for i in range(2, len(nums)-1):
            dp_not_1.append(max(dp_not_1[i-1], dp_not_1[i-2]+nums[i+1]))
        return max(dp[-1], dp_not_1[-1])
