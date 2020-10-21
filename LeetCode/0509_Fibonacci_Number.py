import sys
read = sys.stdin.readline

class Solution:
    def fib(self, N: int) -> int:
    	a, b = 0, 1
    	for _ in range(N):
            a, b = b, a + b
    	return a

'''
        if N==0: return 0
        if N==1: return 1
        fib_list = [0 for _ in range(N+1)]
        fib_list[0] = 0
        fib_list[1] = 1
        for i in range(2,N+1):
            fib_list[i] = fib_list[i-2] + fib_list[i-1]
        return fib_list[N]
'''

'''
        if N==0: return 0
        elif N==1: return 1
        else: return self.fib(N-1)+self.fib(N-2)
'''

num = int(read().rstrip())
mod = Solution()
print(mod.fib(num))

#Runtime: 28 ms, faster than 80.99% of Python3 online submissions for Fibonacci Number.
#Memory Usage: 14 MB, less than 99.99% of Python3 online submissions for Fibonacci Number3
