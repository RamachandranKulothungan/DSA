"""
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
"""


import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        sorted_cars = sorted([(position[i], speed[i]) for i in range(n)], key = lambda x: x[0])
        fleets = 1
        i = n - 1
        multiplier = (target - sorted_cars[i][0])/sorted_cars[i][1]
        while i > -1:
            if sorted_cars[i][0] + sorted_cars[i][1] * multiplier < target:
                multiplier = (target - sorted_cars[i][0])/sorted_cars[i][1]
                fleets += 1
            i = i - 1
        return fleets
            
