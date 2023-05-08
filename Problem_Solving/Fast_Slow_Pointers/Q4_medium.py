"""
Any number will be called a happy number if, after repeatedly replacing 
it with a number equal to the sum of the square of all of its digits, 
leads us to number 1. All other (not-happy) numbers will never reach 1. 
Instead, they will be stuck in a cycle of numbers which does not include 1.

Example-1
Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:
1 - 2**2 + 3**2 = 4 + 9 = 13
2 - 1**1 + 3**3 = 1 + 9 = 10
3 - 1**1 + 0**0 = 1 + 0 = 1
"""
def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = square(slow)
        fast = square(square(fast))

        if slow == fast:
            break
    return slow == 1

def square(num):
    _sum = 0
    while num > 0:
        temp = num % 10
        _sum += temp * temp
        num //= 10
    return _sum

# Time Complexity : O(log N)
# Space Complexity : O(1)

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
