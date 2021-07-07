from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # When the x-values of the first coordinate and the second coordinate are the same
        if coordinates[1][0] == coordinates[0][0]:
            for i in range(2,len(coordinates)):
                if coordinates[0][0]!=coordinates[i][0]:
                    return False

        # When the x-values of the first and second coordinates differ
        else:
            try: # The x-values of the coordinates must all be different, so if the x-values are the same, an exception occurs
                incline = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
                for i in range(2,len(coordinates)):
                    if incline != (coordinates[i][1]-coordinates[0][1])/(coordinates[i][0]-coordinates[0][0]):
                        return False
            except ZeroDivisionError:
                return False
        return True

# class Solution:
#     def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
#         if coordinates[1][0] == coordinates[0][0]:
#             for i in range(2,len(coordinates)):
#                 if coordinates[0][0]!=coordinates[i][0]:
#                     return False
#         else:
#             xs = [coordinates[0][0],coordinates[1][0]]
#             incline = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
#             for i in range(2,len(coordinates)):
#                 if coordinates[i][0] in xs:
#                     return False
#                 xs.append(coordinates[i][0])
#                 if incline != (coordinates[i][1]-coordinates[0][1])/(coordinates[i][0]-coordinates[0][0]):
#                     return False
#         return True

inputs = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
coordinates = []
for e in inputs:
    coordinates.append(list(map(int,e.split(','))))

mod = Solution()
print(mod.checkStraightLine(coordinates))
