class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        water = 0
        while left<right:
            if height[left]<=height[right]:
                curr_water = height[left]*(right-left)
                left = left+1
            else:
                curr_water = curr_water = height[right]*(right-left)
                right = right - 1
            water = max(curr_water, water)
        return water

