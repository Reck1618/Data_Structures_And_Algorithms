"""
Is it possible to advance from the start of the array to the last element 
given that the maximum you can advance from a position is based on the 
value of the array at the index you are currently present on?

Example
[3,3,1,0,2,0,1] - True
[3, 2, 0, 0, 2, 0, 1] - False
"""
def array_advance(A):
    reach = 0
    max_reach = len(A) - 1
    i = 0

    while reach >= i and reach < max_reach:
        reach = max(reach, A[i] + i)
        i += 1
    return reach >= max_reach


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))