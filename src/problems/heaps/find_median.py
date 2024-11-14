"""
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.

https://neetcode.io/problems/find-median-in-a-data-stream
"""





import heapq

class MedianFinder:

    def __init__(self):
        self.even = True
        self.heap_min = []
        self.heap_max = []

    def addNum(self, num: int) -> None:
        if self.even:
            if not self.heap_max:
                heapq.heappush(self.heap_max, -1 * num)
                self.even = False
                return
            if num > -1 * self.heap_max[0]:
                temp = heapq.heappushpop(self.heap_min, num)
                heapq.heappush(self.heap_max, -1 * temp)
            else:
                heapq.heappush(self.heap_max, -1 * num)
            self.even = False        
        else:
            if num >= -1 * self.heap_max[0]:
                heapq.heappush(self.heap_min, num)
            else:
                temp = heapq.heappushpop(self.heap_max, -1 * num)
                heapq.heappush(self.heap_min, -1 * temp)
            self.even = True

    def findMedian(self) -> float:
        print(self.heap_max)
        print(self.heap_min)
        if self.even:
            return (self.heap_min[0] + -1 * self.heap_max[0])/2
        else:
            return -1 * self.heap_max[0]
