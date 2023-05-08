"""
Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  
All the children sit in a line and each of them has a rating score according to his or 
her performance in the class.  Alice wants to give at least 1 candy to each child. 
If two children sit next to each other, then the one with the higher rating must get more candies. 
Alice wants to minimize the total number of candies she must buy.

Example 
INPUT : (6, [4,6,4,5,6,2])
OUTPUT : 10 -> [1,2,1,2,3,1]
"""
def candy(n, arr):
    candies = []
    left = [1] * n
    right = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            left[i] = 1 + left[i - 1]
    
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            right[i] = 1 + right[i + 1]
    
    for i in range(n):
        candies.append(max(left[i], right[i]))
    
    return sum(candies)


def main():
    print(candy(3, [1,2,2]))
    print(candy(10, [2,4,2,6,1,7,8,9,2,1]))

main()