"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only 
Mutually exclusive intervals.

Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].

Example 2:
Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
"""
from heapq import merge


def merge_interval(intervals):
    intervals.sort(key = lambda x:x[0])
    merged = [intervals[0]]

    for start,end in intervals[1:]:
        lastEnd = merged[-1][1]
        if start <= lastEnd:
            merged[-1][1] = max(lastEnd,end)
        else:
            merged.append([start,end])
    return merged

print(merge_interval([[1,4], [2,5], [7,9]]))