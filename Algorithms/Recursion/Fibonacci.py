# Given a number n, return the index value of fibonacci sequence.

# Normal Solution
def normal(n):
    if n < 2:
        return n
    a = 0
    b = 1
    total = 0
    for i in range(n):
        total = a + b
        a = b
        b = total
    return total

# Recursive Solution
def recursive(n):
    if n < 2:
        return n
    else:
        return recursive(n - 1) + recursive(n - 2)

print(recursive(30))
print(normal(100))