class Solution: 
    def characterReplacement(self, s: str, k: int) -> int:
        #inefficient O(N.N)
        # start = 0
        # max_cons = 0
        # end = 0
        # while end<len(s):
        #     char = s[start]
        #     repl_index = start
        #     end = start
        #     replacement = 0
        #     extra_to_left = 0
        #     while replacement<=k:
        #         end = end + 1
        #         if end == len(s):
        #             if replacement<=k:
        #                 extra_to_left = min(k - replacement, start)
        #             break
        #         if s[end]!=char:
        #             if replacement==0:
        #                 repl_index = end
        #             replacement = replacement+1
        #     curr_cons = end-start + extra_to_left
        #     max_cons = max(max_cons, curr_cons)
        #     start = repl_index
        # return max_cons
        
        #O(N)
        start = 0
        end = 0
        frequency_map = {s[start]:1}
        max_consecutive = 0
        while end<len(s):
            if (end-start+1 - max(frequency_map.values())) > k:
                while start<=end:
                    frequency_map[s[start]] = frequency_map[s[start]] - 1
                    start = start + 1
                    if (end-start+1) - max(frequency_map.values())<=k:
                        break
            else:
                curr_consecutive = end-start+1
                max_consecutive = max(curr_consecutive, max_consecutive)
                end = end+1
                if end<len(s):
                    frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1
        return max_consecutive
