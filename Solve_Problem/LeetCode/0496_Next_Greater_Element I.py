from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for e in nums1:
            check = 0
            for i in range(nums2.index(e),len(nums2)):
                if e < nums2[i]:
                        output.append(nums2[i])
                        check = 1
                        break
            if check == 0:
                output.append(-1)
        return output

input_list1 = list(map(int,read().rstrip().split(',')))
input_list2 = list(map(int,read().rstrip().split(',')))
mod = Solution()
print(mod.nextGreaterElement(input_list1, input_list2))
