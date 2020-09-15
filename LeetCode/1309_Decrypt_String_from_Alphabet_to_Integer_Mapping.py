
import sys
read = sys.stdin.readline

class Solution:
    def freqAlphabets(self, s: str) -> str:
        pound_key_order = [e for e,value in enumerate(s) if value=='#']
        for e in pound_key_order:
            s = s.replace(s[e-2], chr(int(s[e-2]+s[e-1])+96))
            s = s.replace(s[e-1], ' ')
            s = s.replace(s[e], ' ')
        print(s)


input_str = read().rstrip()
mod = Solution()
print(mod.freqAlphabets(input_str))
