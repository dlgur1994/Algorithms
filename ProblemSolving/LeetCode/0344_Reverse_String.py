from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

input_str = list(map(str,read().rstrip()))
mod = Solution()
mod.reverseString(input_str)
print(input_str)
