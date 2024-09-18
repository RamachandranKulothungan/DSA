class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #Inefficient due to s_map
        # if t == s:
        #     return t
        # if len(t) > len(s):
        #     return ""
        # t_map = {}
        # for ch in t:
        #     t_map[ch] = t_map.get(ch, 0) + 1
        # required_matches = len(t_map)
        # left,right = 0,0
        # has_match=0
        # s_map = {}
        # min_substr = ""
        # min_window_length = float('inf')
        # while right <= len(s):
        #     if has_match == required_matches:
        #         if min_window_length > len(s[left:right]):
        #             min_window_length = right - left
        #             min_substr = s[left:right]
        #         if s_map[s[left]] == t_map.get(s[left], 0):
        #             has_match = has_match - 1
        #         s_map[s[left]] = s_map[s[left]] - 1
        #         left = left + 1
        #     else:
        #         if right != len(s):
        #             s_map[s[right]] = s_map.get(s[right], 0) + 1
        #             if s_map[s[right]] == t_map.get(s[right], 0):
        #                 has_match = has_match + 1 
        #         right = right+1
        # return min_substr

        if t == s:
            return t
        if len(t) > len(s):
            return ""
        t_map = {}
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1
        required_matches = len(t_map)
        left,right = 0,0
        has_match=0
        min_substr = ""
        min_window_length = float('inf')
        while right <= len(s):
            if has_match == required_matches:
                if min_window_length > len(s[left:right]):
                    min_window_length = right - left
                    min_substr = s[left:right]
                if s[left] in t_map:
                    if t_map.get(s[left]) == 0:
                        has_match = has_match - 1
                    t_map[s[left]] = t_map[s[left]] + 1
                left = left + 1
            else:
                if right != len(s):
                    if s[right] in t_map:
                        t_map[s[right]] = t_map[s[right]] - 1
                        if t_map[s[right]] == 0:
                            has_match = has_match + 1
                right = right+1
        return min_substr
