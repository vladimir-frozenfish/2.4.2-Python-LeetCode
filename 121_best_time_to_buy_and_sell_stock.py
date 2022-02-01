"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""


def maxProfit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0

    minimum_price = prices[0]
    maximum_prise = max(prices[1:])
    profit = maximum_prise - minimum_price
    index_maximum_prize = prices.index(maximum_prise)

    for i in range(1, len(prices) - 1):

        if minimum_price < prices[i]:
            continue

        if index_maximum_prize < i:
            maximum_prise = max(prices[i+1:])
            if maximum_prise == 0:
                break

        profit_temp = maximum_prise - prices[i]
        minimum_price = prices[i]

        if profit_temp > profit:
            profit = profit_temp

    if profit <= 0:
        return 0

    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices) == 5)

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices) == 0)


