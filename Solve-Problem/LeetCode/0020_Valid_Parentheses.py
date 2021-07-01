import sys
read = sys.stdin.readline

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            if stack==[] or e=="(" or e=="[" or e=="{":
                stack.append(e)
            elif e==")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif e=="]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif e=="}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return True if stack ==[] else False

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for e in s:
#             if stack == []:
#                 stack.append(e)
#             elif e==')' and stack[-1]=='(':
#                 stack.pop()
#             elif e=='}' and stack[-1]=='{':
#                 stack.pop()
#             elif e==']' and stack[-1] =='[':
#                 stack.pop()
#             else:
#                 stack.append(e)
#         return True if stack==[] else False

input_str = read().rstrip()
mod = Solution()
print(mod.isValid(input_str))
