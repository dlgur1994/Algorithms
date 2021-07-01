import sys
read = sys.stdin.readline

class Solution:
    def countAndSay(self, n: int) -> str:
        output = [1]
        for i in range(1,n):
            temp = []
            pre = 0
            for j in range(len(output)):
                if output[j] != output[pre]:
                    temp.extend([j-pre,output[pre]])
                    pre = j
                if j == len(output)-1:
                    temp.extend([j-pre+1,output[pre]])
            output = temp
        return ''.join(map(str,output))

input_val = int(read().rstrip())
mod = Solution()
print(mod.countAndSay(input_val))
