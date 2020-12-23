import sys
read = sys.stdin.readline

class Solution:
    def canWinNim(self, n: int) -> bool:
        # If I make the opponent get a multiple of 4, I win and if I get a multiple of 4, I lose.
        return False if n%4 == 0 else True

n = int(read().rstrip())
mod = Solution()
print(mod.canWinNim(n))
