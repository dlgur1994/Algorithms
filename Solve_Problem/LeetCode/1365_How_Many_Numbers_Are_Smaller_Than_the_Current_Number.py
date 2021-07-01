import sys
read = sys.stdin.readline

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int] :
        countList = [0] * 102
        for n in nums:
            countList[n+1] += 1
        for i in range(1,102):
            countList[i] += countList[i-1]
        return [countList[n] for n in nums]

numList = list(map(int,read().split(',')))
mod = Solution()
print(mod.smallerNumbersThanCurrent(numList))
