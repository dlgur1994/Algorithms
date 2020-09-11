import sys
read = sys.stdin.readline

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        numOfJew = 0
        for e in J:
            numOfJew += S.count(e)
        return numOfJew

J = read().rstrip()
S = read().rstrip()
mod = Solution()

print(mod.numJewelsInStones(J, S))
