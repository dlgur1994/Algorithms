
import sys
read = sys.stdin.readline

class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        output = ''

        s = list(s)
        for e in s:
            if e == '#':
                a,b = stack.pop(), stack.pop()
                stack.append(b+a)
            else:
                stack.append(e)

        for e in stack:
            output += chr(int(e)+96)

        return output

input_str = read().rstrip()
mod = Solution()
print(mod.freqAlphabets(input_str))
