import sys
read = sys.stdin.readline

class Solution:
    def countPrimes(self, n: int) -> int:
        eratos = [0,0] + [1]*(n-2)
        i = 2
        while i*i<n:
            if eratos[i]==1:
                eratos[i*i:n:i] = [0] * (1+(n-1-i*i)//i)
            i += 1
        return sum(eratos)

input_val = int(read().rstrip())
mod = Solution()
print(mod.countPrimes(input_val))
