import sys

read = sys.stdin.readline

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a, b = a[:-1], b[:-1] # Remove the 'i' at the back of a and b
        a_real, a_imag = map(int, a.split('+')) # Distinguish a real number from a imaginary number
        b_real, b_imag = map(int, b.split('+'))
        return str(a_real*b_real + -1*a_imag*b_imag) + "+" + str(a_real*b_imag + b_real*a_imag) + "i"

a, b = read().rstrip().split(',')
mod = Solution()
print(mod.complexNumberMultiply(a, b))
