"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""

def generateParenthesis(n):
    result = []
    stack = []

    def backtracking(openN = 0, closeN = 0):
        if openN == closeN == n:
            result.append("".join(stack))
            return
        
        if openN < n:
            stack.append("(")
            backtracking(openN + 1, closeN)
            stack.pop()
        
        if closeN < openN:
            stack.append(")")
            backtracking(openN, closeN + 1)
            stack.pop()
    backtracking()
    return result






print(generateParenthesis(3))