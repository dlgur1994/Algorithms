import sys
read = sys.stdin.readline

class Solution:
    def isPalindrome(self, x: int) -> bool:
            if x>=0 and str(x)==str(x)[::-1]:
                return True
            return False

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#             if x<0:
#                 return False
#             x_str = str(x)
#             for i in range(len(x_str)//2):
#                 if x_str[i] != x_str[len(x_str)-1-i]:
#                     return False
#             return True

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x<0:
#             return False
#         nums = []
#         while True:
#             if x<10:
#                 nums.append(x)
#                 break
#             nums.append(int(x%10))
#             x //= 10
#         for i in range(len(nums)//2):
#             if nums[i] != nums[len(nums)-1-i]:
#                 return False
#         return True

input_val = int(read().rstrip())
mod = Solution()
print(mod.isPalindrome(input_val))
