import sys
read = sys.stdin.readline

class Solution:
    input = int(read())
    result = subtractProductAndSum(input)
    print(result)
    
    def subtractProductAndSum(self, n: int) -> int:
        lenOfNum = len(str(n))
        arr = [None] * lenOfNum

        i=0
        product = 1
        sum = 0
        for _ in range(0,lenOfNum):
            arr[i] = int(n%10)
            n = n/10
            product *= arr[i]
            sum += arr[i]
            i = i+1

        return product-sum
