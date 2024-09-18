class Solution:
    def twoSum(self, nums, target: int) -> list[int]:
        value_map = {}
        for i in range(len(nums)):
            required_prev = target - nums[i]
            print(required_prev)
            if value_map.get(required_prev) is not None:
                return [value_map[required_prev], i]
            value_map[nums[i]] = i
            print(value_map)


print(Solution().twoSum([3, 4, 5, 6], 7))
