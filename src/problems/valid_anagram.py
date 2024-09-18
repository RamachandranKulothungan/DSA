class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map_s = {}
        char_map_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if char_map_s.get(s[i]):
                char_map_s[s[i]] += 1
            else:
                char_map_s[s[i]] = 1
            if char_map_t.get(t[i]):
                char_map_t[t[i]] += 1
            else:
                char_map_t[t[i]] = 1
        if len(char_map_s.keys()) != len(char_map_t.keys()):
            return False
        return char_map_t == char_map_s
