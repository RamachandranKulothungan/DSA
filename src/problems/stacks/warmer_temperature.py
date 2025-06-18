"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a 
future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
"""

from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        brute force:
        n^2: loop through each element then check all future elements to find the next possible temperature
        
        extra space:
        O: n
        S: store stack of next largest elements: [(temp, index)]
        start from right end:
        if S empty: result[i]=0
        if not empty: pop items until we find an item with greater temp is found.
            result[i] = item(index)
            append item i to stack
        """
        result=deque([])
        stack = []
        for i, temperature in enumerate(temperatures[-1::-1]):
            while stack and stack[-1][1]<=temperature:
                stack.pop()
            if stack:   result.appendleft(i - stack[-1][0])
            else:   result.appendleft(0)
            stack.append((i, temperature))
        return list(result)

            

        