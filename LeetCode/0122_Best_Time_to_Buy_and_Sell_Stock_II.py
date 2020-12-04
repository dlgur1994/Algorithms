from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy = prices[0]
#         profit = 0
#         for i in range(1,len(prices)-1):
#             if prices[i] < buy:
#                 buy = prices[i]
#             if prices[i] > prices[i+1]:
#                 profit += prices[i] - buy
#                 buy = prices[i+1]
#         if prices[-1]>buy:
#             profit += prices[-1] - buy
#         return profit

input_list = list(map(int, read().rstrip().split(',')))
mod = Solution()
print(mod.maxProfit(input_list))
