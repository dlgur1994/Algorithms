import sys
read = sys.stdin.readline

class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    map = [1 for i in range(m*n)]
    for i in range(n, m*n):
      if (i%n) != 0:
        map[i] = map[i-1] + map[i-n]  
    print(map)
    return map[-1] 

# class Solution:
#   def uniquePaths(self, m: int, n: int) -> int:
#     map = [0 for i in range(m*n)]
#     for i in range(len(map)):
#       if i < n:
#         map[i] = 1
#       elif i%n == 0:
#         map[i] = 1
#       else:
#         map[i] = map[i-1] + map[i-n]
#     return map[-1]  

m, n = map(int, read().split(' '))
mod = Solution()
print(mod.uniquePaths(m,n))