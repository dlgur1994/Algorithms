import sys

read = sys.stdin.readline

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            mid1,mid2 = i,i # suppose the length of the string looked for is odd
            while mid1>-1 and mid2<len(s) and s[mid1]==s[mid2]:
                mid1 -= 1
                mid2 += 1
                ans += 1
            mid1,mid2 = i,i+1 # suppose the length of the string looked for is even
            while mid1>-1 and mid2<len(s) and s[mid1]==s[mid2]:
                mid1 -= 1
                mid2 += 1
                ans += 1
        return ans

# time limit exceeded
# class Solution:
#     def checkSymm(self, s):
#         for i in range(len(s)//2):
#             if s[i] != s[len(s)-i-1]:
#                 return False
#         return True
#
#     def countSubstrings(self, s: str) -> int:
#         l = len(s)
#         ans = 0
#         for i in range(l):
#             for j in range(i, l):
#                 if self.checkSymm(s[i:j+1]):
#                     ans += 1
#         return ans

s = read().rstrip()
mod = Solution()
print(mod.countSubstrings(s))
