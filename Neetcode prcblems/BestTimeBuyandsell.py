from typing import List

"""Chat GPT Solution"""
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')  # precio mínimo encontrado hasta ahora
#         max_profit = 0            # máxima ganancia encontrada

#         for price in prices:
#             if price < min_price:
#                 min_price = price  # actualiza el mínimo
#             else:
#                 profit = price - min_price  # posible ganancia hoy
#                 max_profit = max(max_profit, profit)  # actualiza el máximo

#         return max_profit
    

"""Brute Solution"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res
    

"""Two pointers solution"""

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r = 0, 1
#         maxP = 0

#         while r < len(prices):
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 maxP = max(maxP, profit)
#             else:
#                 l = r
#             r += 1
#         return maxP

"""Dynamic Programming Solution"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP

prices = [10,1,5,6,7,1]

s = Solution()
print(s.maxProfit(prices))