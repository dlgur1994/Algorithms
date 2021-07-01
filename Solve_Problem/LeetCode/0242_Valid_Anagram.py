from collections import Counter
import sys
read = sys.stdin.readline

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         for e in s:
#             if s.count(e) != t.count(e):
#                 return False
#         return True

str1, str2 = read().rstrip().split(',')
mod = Solution()
print(mod.isAnagram(str1, str2))
