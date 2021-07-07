import sys
read = sys.stdin.readline

class Solution:
    def isHappy(self, n: int) -> bool:
        cycle_list = []
        while True:
            sum = 0
            for i in range(len(str(n))):
                sum += (int(n%10))**2
                n /= 10
            if sum in cycle_list:
                return False
            cycle_list.append(sum)
            if sum == 1:
                return True
            n = sum

input_num = int(read().rstrip())
mod = Solution()
print(mod.isHappy(input_num))
