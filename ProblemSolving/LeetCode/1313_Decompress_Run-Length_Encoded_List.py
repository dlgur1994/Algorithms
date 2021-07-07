import sys
read = sys.stdin.readline

class Solution:
    def decompressRLElist(self, nums):
        result = []
        for i in range(0,len(nums)//2):
            result += [nums[2*i+1]] * nums[2*i] 
        return result

numList = list(map(int,read().split(',')))
mod = Solution()
print(mod.decompressRLElist(numList))
