import sys
read = sys.stdin.readline

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        first = s[0]
        numOfSame = 1
        numOfBal = 0

        for i in range(1,len(s)):
            if first == s[i]:
                numOfSame += 1
            else:
                numOfSame -= 1
            if numOfSame == 0:
                numOfBal += 1

        return numOfBal

input = read()
mod = Solution()
print(mod.balancedStringSplit(input))
