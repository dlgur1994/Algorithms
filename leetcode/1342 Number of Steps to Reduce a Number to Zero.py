import sys
read = sys.stdin.readline

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num > 0:
            if num%2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1
        return count

num = int(read())
mod = Solution()
print(mod.numberOfSteps(num))
