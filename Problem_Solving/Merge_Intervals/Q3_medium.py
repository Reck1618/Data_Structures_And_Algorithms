"""
Given two lists of intervals, find the intersection of these two lists. 
Each list consists of disjoint intervals sorted on their start time.

Example 1:
Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Example 2:
Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""

#Method-1
def merge_1(A, B):
    merged = []
    i,j = 0,0

    while i < len(A) and j < len(B):
        low = max(A[i][0],B[j][0])
        high = min(A[i][1],B[j][1])

        if low <= high:
            merged.append([low,high])

        if A[i][1] <= B[j][1]:
            i += 1
        else:
            j += 1
            
    return merged 


print(merge_1([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))


#Method-2
def merge_2(A, B):
    merged = []
    i,j,start,end = 0,0,0,1

    while i < len(A) and j < len(B):
        a_overlaps_b = A[i][start] >= B[j][start] and A[i][start] <= B[j][end]
        b_overlaps_a = B[j][start] >= A[i][start] and B[j][start] <= A[i][end]

        if a_overlaps_b or b_overlaps_a:
            merged.append([max(A[i][start],B[j][start]),min(A[i][end],B[j][end])])

        if A[i][end] < B[j][end]:
            i += 1
        else:
            j += 1
    return merged


print(merge_2([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))