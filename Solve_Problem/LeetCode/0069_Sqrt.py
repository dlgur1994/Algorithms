import sys
read = sys.stdin.readline

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         cnt = 1
#         while True:
#             if cnt*cnt > x:
#                 return cnt-1
#             cnt += 1

input_val = int(read().rstrip())
mod = Solution()
print(mod.mySqrt(input_val))
