"""
Given two integer arrays to represent weights and profits of N items, we need to find a 
subset of these items which will give us maximum profit such that their cumulative weight 
is not more than a given number C. Each item can only be selected once, which means either 
we put an item in the knapsack or we skip it.
"""

def solve_knapsack(profits, weights, capacity):
    return solve(profits, weights, capacity, 0)

def solve(profits, weights, capacity, cur_index):

    if capacity <= 0 or cur_index >= len(weights):
        return 0 

    profit1 = 0
    if weights[cur_index] <= capacity:
        profit1 = profits[cur_index] + solve(profits, weights, capacity - weights[cur_index], cur_index + 1)
    
    profit2 = solve(profits, weights, capacity, cur_index + 1)

    return max(profit1, profit2)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))

main()