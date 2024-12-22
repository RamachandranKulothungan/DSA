"""
Each clip is a string of length = clipLength, and consists of only lowercase english characters.
A clip is smooth if difference between any two adjacent characters of the clip differ by a difference of diff or less.
Example: clipLength = 2, diff = 3
aa = valid, differnece = 0
ab = valid, differnece = 1
xy = valid, differnece = 1
az = invalid, differnece = 25
za = invalid, differnece = 25

Inputs:
clipLength
diff
"""
