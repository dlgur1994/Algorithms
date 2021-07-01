import sys

read = sys.stdin.readline

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack, need = 0, 0 # 'stack' is the number of '(', and 'need' is the number of '(' required to make a parenthesis valid
        for e in S:
            if e == ')': # when the character is ')'
                if stack > 0: # when '(' appeared before
                    stack -= 1
                else: # it means '(' is needed to make a parenthesis valid
                    need += 1
            else: # when the character is '(', add one to 'stack'
                stack += 1
        return need+stack

S = read().rstrip()
mod = Solution()
print(mod.minAddToMakeValid(S))
