'''
Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
def max_profit(prices):
    n = len(prices)
    maxProfit = 0

    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                print(prices[j],"-", prices[i], "=",profit)

                maxProfit = max(maxProfit, profit)
    
    return maxProfit

# Main
prices = [7,1,5,3,6,4]
print("Max profit",max_profit(prices))

# ? Time Complexity: O(n^2) as we are using two nested loops

# ? Space Complexity: O(1) as we are not using any extra space