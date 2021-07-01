from typing import List
import sys

read = sys.stdin.readline


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1, num+1): # You have to find the rules by writing it yourself
            if i%2 == 1:
                dp.append(dp[i-1]+1)
            else:
                dp.append(dp[i//2])
        return dp

# best answer, but too much
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         ans = [0]
#         cnt = 1
#         while cnt <= num:
#             new_digit = cnt & (cnt-1)
#             if new_digit == 0:
#                 new_ans = [a+1 for a in ans]
#                 ans += new_ans
#                 cnt += len(new_ans)
#         return ans[:num+1]

# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         output = []
#         for n in range(num+1):
#             output.append((str(bin(n)).count("1")))
#         return output

num = int(read().rstrip())
mod = Solution()
print(mod.countBits(num))
