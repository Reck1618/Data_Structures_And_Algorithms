"""
You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money. Return the fewest number of coins that 
you need to make up that amount. If that amount of money cannot be made up by any combination 
of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

 Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
"""
# Dynamic Programming
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(amount + 1):
        for c in coins:
            dp[i] = min(dp[i], 1 + dp[i - c])
    
    return dp[amount] if dp[amount] != amount + 1 else -1


# Backtracking - BruteForce
def coin_change_1(coins, amount):
    ans = {}

    def Backtracking(amount, cur_arr = []):
        if amount <= 0:
            if amount == 0:
                ans[len(cur_arr)] = cur_arr[:]
            return 
        
        for i in range(len(coins)):
            cur_arr.append(coins[i])
            Backtracking(amount - coins[i], cur_arr )
            cur_arr.pop()
        
    Backtracking(amount)
    return min(ans)


def main():
    print(coin_change([1,2,5], 100))
    print(coin_change_1([1,2,5], 25)) # Max = 265

main()