"""
Given two integer arrays to represent weights and profits of N items, we need to find a 
subset of these items which will give us maximum profit such that their cumulative weight 
is not more than a given number C. Each item can only be selected once, which means either 
we put an item in the knapsack or we skip it.
"""

def solve_knapsack(profits, weights, capacity):

    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for i in range(capacity + 1)] for j in range(n)]

    for i in range(0,n):
        dp[i][0] = 0
    
    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0

            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]

            profit2 = dp[i - 1][c]

            dp[i][c] = max(profit1, profit2)
    print_selected_items(dp, profits, weights, capacity)
    return dp[n - 1][capacity]

def print_selected_items(dp, profits, weights, capacity):
    print("Selected weights are: ", end="")
    n = len(weights)
    totalProfit = dp[n - 1][capacity]

    for i in range(n - 1, 0, -1):
        if totalProfit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end="")
            capacity -= weights[i]
            totalProfit -= profits[i]
        
    if totalProfit != 0:
        print(str(weights[0]) + " ", end="")
    print()
    



def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()