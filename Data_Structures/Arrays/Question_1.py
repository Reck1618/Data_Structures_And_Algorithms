# Create a Function that reverses a string in python.

def string_reverse_1(string):
    return string[::-1]

print(string_reverse_1("hello"))


def string_reverse_2(string):
    ans = ""
    for i in range(len(string) -1, -1, -1):
        ans += "".join(string[i])
    return ans

print(string_reverse_2("hello"))