class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)

        left = 0
        right = n - 1
        minimum = nums[left]
        while left < right:
            print(left, right)
            if nums[left] <= nums[right]:
                minimum = min(minimum, nums[left])
                break
            m = int((left + right) / 2)
            if nums[m] > nums[left]:
                left = m
            else:
                minimum = min(minimum, nums[m])
                right = m
        return minimum


print(Solution().findMin([x for x in range(5, 10)] + [x for x in range(1, 5)]))
