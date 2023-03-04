# Calculate the factorial of a given number

# Normal Solution
def normal(num):
    ans = 1
    for i in range(1, num + 1):
        ans *= i
    return ans

# Recursive Solution
def recursion(num):
    if num == 1 or num == 0:                # Base Case
        return 1
    else:                                   # Function Call
        return num * recursion(num - 1)




print(normal(2))
print(recursion(2))