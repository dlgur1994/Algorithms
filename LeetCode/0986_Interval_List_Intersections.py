from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def intervalIntersection(self, first_list: List[List[int]], second_list: List[List[int]]) -> List[List[int]]:
        if first_list==[] or second_list==[]: # if either of the two is empty
            return []
        ans = []
        cnt1, cnt2 = 0, 0
        while True:
            if first_list[cnt1][1] < second_list[cnt2][0]: # when the range of the second list element is greater than the range of the first list element
                cnt1 += 1
            elif first_list[cnt1][0] > second_list[cnt2][1]: # when the range of the first list element is greater than the range of the second list element
                cnt2 += 1
            elif first_list[cnt1][0]<=second_list[cnt2][0] and first_list[cnt1][1]>=second_list[cnt2][1]: # when the first list element contains the second list element
                ans.append(second_list[cnt2])
                cnt2 += 1
            elif first_list[cnt1][0]>=second_list[cnt2][0] and first_list[cnt1][1]<=second_list[cnt2][1]: # when the second list element contains the first list element
                ans.append(first_list[cnt1])
                cnt1 += 1
            elif first_list[cnt1][0]<=second_list[cnt2][0] and first_list[cnt1][1]<=second_list[cnt2][1]: # when the two elements overlap
                ans.append([second_list[cnt2][0],first_list[cnt1][1]])
                cnt1 += 1
            elif first_list[cnt1][0]>=second_list[cnt2][0] and first_list[cnt1][1]>=second_list[cnt2][1]: # when the two elements overlap
                ans.append([first_list[cnt1][0],second_list[cnt2][1]])
                cnt2 += 1
            if cnt1==len(first_list) or cnt2==len(second_list): # if either list ends
                return ans

first_list = []
second_list = []
temp1 = read().rstrip().lstrip('[').rstrip(']').split('],[')
temp2 = read().rstrip().lstrip('[').rstrip(']').split('],[')
for e in temp1:
    first_list.append(list(map(int,e.split(','))))
for e in temp2:
    second_list.append(list(map(int,e.split(','))))
mod = Solution()
print(mod.intervalIntersection(first_list,second_list))
