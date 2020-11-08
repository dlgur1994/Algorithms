import sys
read = sys.stdin.readline

class Solution:
    def binaryGap(self, n: int) -> int:
        cnt = 0
        check_list = []
        while n>1:
            if int(n%2) == 1:
                check_list.append(cnt)
            cnt += 1
            n //= 2
        if n == 1:
            check_list.append(cnt)

        max_len = 0
        for i in range(len(check_list)-1):
            lens = check_list[i+1] - check_list[i]
            if lens>max_len:
                max_len = lens
        return max_len

input_val = int(read().rstrip())
mod = Solution()
print(mod.binaryGap(input_val))
