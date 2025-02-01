"""
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
"""


class Solution:
    def trap(self, height) -> int:
        max_water = 0
        left_tower_stack = []
        for i, tower in enumerate(height):
            curr_max_water = 0
            base_height = 0
            while True:
                if left_tower_stack:
                    if tower >= height[left_tower_stack[-1]]:
                        curr_max_water += (
                            min(tower, height[left_tower_stack[-1]]) - base_height
                        ) * (i - left_tower_stack[-1] - 1)
                        base_height = height[left_tower_stack[-1]]
                        left_tower_stack.pop()
                    else:
                        curr_max_water += (
                            min(tower, height[left_tower_stack[-1]]) - base_height
                        ) * (i - left_tower_stack[-1] - 1)
                        break
                else:
                    break
            max_water += curr_max_water
            left_tower_stack.append(i)
        return max_water
