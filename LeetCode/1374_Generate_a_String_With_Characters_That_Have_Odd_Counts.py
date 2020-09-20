import sys
read = sys.stdin.readline

class Solution:
    def generateTheString(self, n: int) -> str:
        output = ''
        if n%2==0:
            output += 'a'
        else:
            output += 'b'
        for _ in range(1,n):
            output += 'b'
        return output
        
input_num = int(read().rstrip())
mod = Solution()
print(mod.generateTheString(input_num))
