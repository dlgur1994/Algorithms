import sys
read = sys.stdin.readline

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A)==1 or len(B)==1: return False
        diff = []
        for i in range(len(A)):
            if A[i] != B[i]: diff.append(i)
        if len(diff)==0:
            for e in A:
                temp = list(A[:])
                temp.remove(e)
                if e in temp: return True
        if len(diff) != 2: return False
        if A[diff[0]]==B[diff[1]] and A[diff[1]] == B[diff[0]]: return True
        return False

input_A, input_B = read().rstrip().split(',')
mod = Solution()
print(mod.buddyStrings(input_A, input_B))
