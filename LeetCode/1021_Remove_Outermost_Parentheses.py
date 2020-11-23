import sys
read = sys.stdin.readline

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        temp = []
        output = []
        for e in S:
            stack.pop() if e == ')' else stack.append(e)
            temp.append(e)
            if stack == []:
                del temp[0]
                temp.pop()
                output.extend(temp)
                temp = []
        return ''.join(output)

input_str = read().rstrip()
mod = Solution()
print(mod.removeOuterParentheses(input_str))
