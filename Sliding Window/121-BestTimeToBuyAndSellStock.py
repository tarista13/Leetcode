"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Ex 1:

Input: prices = [7,1,5,3,6,4]
Output: 5

Ex 2:
Input: prices = [7,6,4,3,1]
Output: 0
"""

def maxProfit(prices):
    l, r = 0, 1
    profit = 0
    while r < len(prices):
        if prices[r] > prices[l]:
            currProfit = prices[r] - prices[l]
            profit = max(profit, currProfit)
        else:
            l = r
        r += 1
    return profit


prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

print(maxProfit(prices1))
print(maxProfit(prices2))