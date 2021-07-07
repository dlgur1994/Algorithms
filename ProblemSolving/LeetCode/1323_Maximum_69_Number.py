import sys
read = sys.stdin.readline

class Solution:
    def maximum69Number (self, num: int) -> int:
        max = int(num)
        #numList = [int(x) for x in str(num)]
        numList = list(map(int, str(num)))
        numList2 = numList[:]
        for i in range(0,len(numList2)):
            numList2[i] = 9 if numList2[i]==6 else 6
            temp = int("".join(map(str,numList2)))
            if temp > max:
                max = temp
            numList2 = numList[:]
        return max

num = read().rstrip()
mod = Solution()
print(mod.maximum69Number(num))
