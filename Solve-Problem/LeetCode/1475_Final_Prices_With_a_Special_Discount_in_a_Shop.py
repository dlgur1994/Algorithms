from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(0,len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break

        return prices

input = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
mod = Solution()
print(mod.finalPrices(input))
