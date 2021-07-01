from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(s, bal):
            if len(s) == 2*n: # when s is completed
                return result.append(s)
            else:
                if bal == 0:
                    dfs(s+"(", bal+1 )
                else :
                    if s.count("(") < n:
                        dfs(s+"(",bal+1)
                    dfs(s+")",bal-1)

        result = []
        dfs("(",1)
        return result

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         def dfs(s, bal):
#             if len(s) == 2*n:
#                 return result.append(s)
#             else:
#                 if bal == 0:
#                     dfs(s+"(", bal+1 )
#                 else :
#                     if s.count("(") < n:
#                         dfs(s+"(",bal+1)
#                     dfs(s+")",bal-1)
#
#         result = []
#         dfs("(",1)
#         return result

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         def generateOptions(s):
#             if len(s) == 2*n:
#                 if isValid(s) == 0:
#                  ans.append(''.join(s))
#             else:
#                 s.append('(')
#                 generateOptions(s)
#                 s.pop()
#                 s.append(')')
#                 generateOptions(s)
#                 s.pop()
#
#         def isValid(s):
#             stack = 0
#             for e in s:
#                 if e == '(':
#                     stack += 1
#                 else:
#                     stack -= 1
#                 if stack < 0:
#                     return -1
#             return stack
#
#         ans = []
#         generateOptions([])
#         return ans

n = int(read().rstrip())
mod = Solution()
print(mod.generateParenthesis(n))
