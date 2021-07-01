import sys
read = sys.stdin.readline

class Solution:
    def divisorGame(self, N: int) -> bool:
        if N%2 == 0:
            return True
        else:
            return False

input_val = int(read().rstrip())
mod = Solution()
print(mod.divisorGame(input_val))
