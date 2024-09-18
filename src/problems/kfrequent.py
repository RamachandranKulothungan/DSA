class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        freq_list = sorted(
            frequency_map.keys(), key=lambda key: frequency_map[key], reverse=True
        )
        return freq_list[:k]


print(Solution().topKFrequent([1, 2, 2, 3, 4, 5, 6, 6, 6], 2))
