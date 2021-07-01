import sys
read = sys.stdin.readline

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        # change x and y to binary
        new_x, new_y = format(x, "b"), format(y, "b")
        # new_x, new_y = bin(x)[2:], bin(y)[2:]

        #find the short binary and the long binary
        if len(new_x)<len(new_y):
            short, long = new_x, new_y
        else:
            short, long = new_y, new_x

        #add the number of 1 in the long over length of the short to cnt
        cnt += long[:-(len(short))].count("1")

        #Compare the binary number of the short and the long and add 1 to cnt if different.
        for i in range(1,len(short)+1):
            if short[-i] != long[-i]:
                cnt += 1
        return cnt

x, y = map(int, read().rstrip().split(','))
mod = Solution()
print(mod.hammingDistance(x, y))
