class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        number_map = {}
        for i in nums:
            if i in number_map.keys():
                return True
            number_map[i] = 1
        return False


print(Solution().containsDuplicate([1, 2, 3, 4]))
