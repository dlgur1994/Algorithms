import sys
read = sys.stdin.readline

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for e in s:
            if e in t:
                idx = t.index(e)
                t = t[idx+1:]
            else:
                return False
        return True

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         cnt = 0
#         temp = []
#         for e in s:
#             while cnt < len(t):
#                 if e == t[cnt]:
#                     cnt += 1
#                     temp.append(e)
#                     break
#                 cnt += 1
#             if cnt==len(t) and len(temp)!=len(s):
#                 return False
#         return True

str1, str2 = read().rstrip().split(',')
mod = Solution()
print(mod.isSubsequence(str1, str2))
