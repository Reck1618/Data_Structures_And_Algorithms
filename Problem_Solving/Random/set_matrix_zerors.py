"""
Given an m x n integer matrix matrix, if an element is 0, 
set its entire row and column to 0's. You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
# Space - O(m+n)
def setZeroes_1(matrix):
    row = set()
    column = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                column.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row or j in column:
                matrix[i][j] = 0
    return matrix

def main():
    print(setZeroes_1([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
main()


# Space - O(1)
def setZeroes_2(matrix):
    rows, columns = len(matrix), len(matrix[0])
    rowzero = False
    
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowzero = True
    
    for r in range(1, rows):
        for c in range(1, columns):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
    
    if rowzero:
        for c in range(columns):
            matrix[0][c] = 0
    
    return matrix

def main_1():
    print(setZeroes_2([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
main_1()