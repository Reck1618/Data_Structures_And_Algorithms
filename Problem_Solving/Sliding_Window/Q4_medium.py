"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. 
You will be given two baskets, and your goal is to pick as many fruits as possible 
to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. 
The farm has following restrictions:

1-Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
2-You can start with any tree, but you can't skip a tree once you have started.
3-You will pick exactly one fruit from every tree until you cannot, i.e., 
you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Example
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
"""
def fruits_into_baskets(arr):
    store = {}
    start = 0
    length = 0

    for i in range(len(arr)):
        if arr[i] in store:
            store[arr[i]] += 1
        else:
            store[arr[i]] = 1
        
        while len(store) > 2:
            if store[arr[start]] == 1:
                del store[arr[start]]
            else:
                store[arr[start]] -= 1
            start += 1

        length = max(length, (i - start + 1))

    return length

# Time Complexity = O(N)
# Space Complexity = O(1)

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
