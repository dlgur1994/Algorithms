from typing import List
from itertools import combinations
import sys
read = sys.stdin.readline

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        bits = ['0','1','2','3','4','5','6','7','8','9']
        minuts = {'0':1, '1':2, '2':4, '3':8, '4':16, '5':32}
        hours = {'6':1, '7':2, '8':4, '9':8}

        #Use all possible combinations of numbers
        ons = list(combinations(bits, num))
        times = []
        for on in ons:
            hour = 0
            minut = 0
            for e in on:
                if e in minuts:
                    minut += minuts[e]
                else:
                    hour += hours[e]
            if hour>11 or minut>59:
                continue
            #to fit the two-digit format in minutes
            times.append("%d:%02d" %(hour, minut))
        return times

# class Solution:
#     def readBinaryWatch(self, num):
#         def dfs(start, cnt, hours, mins):
#             if hours > 11 or mins > 59:
#                 return
#             if cnt == num:
#                 times.append("%d:%02d" % (hours, mins))
#                 return
#             for i in range(start, 10):
#                 if i < 4:
#                     dfs(i+1, cnt+1, hours+hm[i], mins)
#                 else:
#                     dfs(i+1, cnt+1, hours, mins+hm[i])
#
#         times, hm = [], [8,4,2,1,32,16,8,4,2,1]
#         dfs(0, 0, 0, 0)
#         return times

input_val = int(read().rstrip())
mod = Solution()
print(mod.readBinaryWatch(input_val))
