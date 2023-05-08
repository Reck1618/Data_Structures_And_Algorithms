"""
Problem 1: Given a set of intervals, find out if any two intervals overlap.

Example:
Intervals: [[1,4], [2,5], [7,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap
"""

def overlap(intervals):
    intervals.sort(key = lambda x:x[0])
    temp = intervals[0]

    for start,end in intervals[1:]:
        lastEnd = temp[1]
        if start <= lastEnd:
            return True
        else:
            temp = [start,end]
    return False

print(overlap([[1,4], [3,5], [7,9]]))