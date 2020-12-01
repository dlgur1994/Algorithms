import sys
read = sys.stdin.readline

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for price in prices:


input_list = list(map(int, read().rstrip().split(',')))
mod = Solution()
print(mod.maxProfit(input_list))
