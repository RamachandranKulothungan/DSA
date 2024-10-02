class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            print(left, right)
            m = int((left + right) / 2)
            if nums[m] == target:
                return m
            if nums[right] > nums[m]:
                if target > nums[m] and target <= nums[right]:
                    left = m + 1
                else:
                    right = m
            else:
                if target < nums[m] and target >= nums[left]:
                    right = m
                else:
                    left = m + 1
        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
