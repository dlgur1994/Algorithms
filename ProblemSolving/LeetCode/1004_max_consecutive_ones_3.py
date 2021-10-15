import sys
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        arr = []
        flag, cnt = 1, 0
        if nums[0] == 0: arr.append(0)
        for i in range(len(nums)):
            if nums[i] == 1:
                if flag == 1: cnt += 1
                else:
                    flag, cnt = 1, 1
                if i == len(nums)-1 or nums[i+1] == 0:
                    arr.append(cnt)
            else:
                if flag == 0: cnt += 1
                else:
                    flag, cnt = 0, 1
                if i == len(nums)-1 or nums[i+1] == 1:
                    arr.append(cnt)
        print(arr)
        # if arr[2*i+1] < k:
        #     return arr[2*i] + arr[2*i+1] + arr[2*i+2]
        # else:
        #     return max[arr] + k

nums = list(map(int, sys.stdin.readline().rstrip().split(',')))
k = int(sys.stdin.readline().rstrip())
mod = Solution()
print(mod.longestOnes(nums,k))