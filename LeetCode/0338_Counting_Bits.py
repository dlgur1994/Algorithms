from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def countBits(self, num: int) -> List[int]:
        output = []
        for n in range(num+1):
            output.append((str(bin(n)).count("1")))
        return output

num = int(read().rstrip())
mod = Solution()
print(mod.countBits(num))
