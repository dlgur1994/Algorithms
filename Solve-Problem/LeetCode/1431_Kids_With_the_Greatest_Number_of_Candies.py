from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output_list = []
        for candy in candies:
            if candy+extraCandies >= max(candies):
                output_list.append(True)
            else:
                output_list.append(False)
        return output_list

dump = list(map(int,read().rstrip()))
input_list = dump[:len(dump)-1]
input_candies = dump[-1]
mod = Solution()
print(mod.kidsWithCandies(input_list,input_candies))
