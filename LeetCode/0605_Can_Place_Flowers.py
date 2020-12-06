from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i-1]+flowerbed[i+1] == 0:
                flowerbed[i] = 1
                cnt += 1
        return cnt >= n

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if len(flowerbed)<3:
#             if 1 not in flowerbed and n<=1:
#                 return True
#             elif 1 in flowerbed and n==0:
#                 return True
#             else:
#                 return False
#         cnt = 0
#         if flowerbed[0]==0 and flowerbed[1]==0:
#             flowerbed[0]=1
#             cnt += 1
#         if flowerbed[-2]==0 and flowerbed[-1]==0:
#             flowerbed[-1]=1
#             cnt += 1
#         print(flowerbed)
#         for i in range(len(flowerbed)-2):
#             if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i+2]==0:
#                 cnt += 1
#                 flowerbed[i+1] = 1
#                 i += 1
#         return cnt >= n

input_list = list(map(int,read().rstrip().split(',')))
input_int = int(read().rstrip())
mod = Solution()
print(mod.canPlaceFlowers(input_list, input_int))
