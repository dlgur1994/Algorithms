import sys
read = sys.stdin.readline


class Solution:
    def findNumbers(self, nums) -> int:
        numOfEven = 0

        for e in nums:
            if len(str(e))%2 == 0:
                numOfEven += 1

        return numOfEven

numInputs = list(map(str,read().rstrip('\n').split(',')))
output = Solution()
result = output.findNumbers(numInputs)
print(result)
