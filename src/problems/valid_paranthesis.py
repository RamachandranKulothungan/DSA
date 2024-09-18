class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_p = []
        closeopen_p_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        opening_p_set = {"(","{","["}
        for ch in s:
            if ch in opening_p_set:
                stack_p.append(ch)
            elif ch in closeopen_p_map.keys():
                if not stack_p or stack_p[-1] != closeopen_p_map[ch]:
                    return False
                stack_p.pop()
        if stack_p:
            return False
        return True
