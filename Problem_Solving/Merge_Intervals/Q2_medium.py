"""
Given a list of non-overlapping intervals sorted by their start time, 
Insert a given interval at the correct position and merge all necessary intervals 
To produce a list that has only mutually exclusive intervals.

Example 1:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Example 2:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Example 3:
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""

#Method-1
def insert_interval_1(intervals,new_int):
    merged = []

    for i in range(len(intervals)):
        if new_int[1] < intervals[i][0]:
            merged.append(new_int)
            return merged + intervals[i:]
        elif intervals[i][1] < new_int[0]:
            merged.append(intervals[i])
        else:
            new_int = [min(new_int[0],intervals[i][0]),max(new_int[1],intervals[i][1])]
    
    merged.append(new_int)
    return merged

print(insert_interval_1([[1,3], [5,7], [8,12]], [4,6]))


#Method-2 : fast
def insert_interval_2(intervals,new_int):
    merged = []
    i,start,end = 0,0,1

    while i < len(intervals) and intervals[i][end] < new_int[start]:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] <= new_int[end]:
        new_int = [min(new_int[start], intervals[i][start]),max(new_int[end],intervals[i][end])]
        i += 1
    
    merged.append(new_int)
    return merged + intervals[i:]

print(insert_interval_2([[1,3], [5,7], [8,12]], [4,6]))