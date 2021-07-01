from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        max_prof = 0
        min_buy = prices[0]
        for price in prices:
            min_buy = min(min_buy,price)
            max_prof = max(max_prof,price-min_buy)
        return max_prof

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_prof = 0
#         for i in range(len(prices)-1):
#             temp = prices[i+1:]
#             if max(temp)-prices[i] > 0 and max(temp)-prices[i] > max_prof:
#                 max_prof = max(temp) - prices[i]
#         return max_prof

input_list = list(map(int,read().rstrip().split(',')))
mod = Solution()
print(mod.maxProfit(input_list))
