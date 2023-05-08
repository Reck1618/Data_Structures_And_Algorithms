"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock. Return the maximum profit you can achieve 
from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
"""

def maxProfit(prices):
    max_profit = 0
    buy = prices[0]

    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - buy)
        buy = min(buy, prices[i])

    return max_profit

def main():
    print(maxProfit([7,1,5,3,6,4]))

main()