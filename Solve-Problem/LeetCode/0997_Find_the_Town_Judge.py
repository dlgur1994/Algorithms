from typing import List
import sys

read = sys.stdin.readline

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # followers of each person
        followers = [[0] for i in range(N+1)]
        # candidates who can be a judge
        candidates = [i for i in range(0,N+1)]
        judge = -1
        # if there is only one person, the person is the judge
        if N == 1:
            judge = 1
        elif N > 1:
            for e in trust:
                followers[e[1]].append(e[0])
                # if a person follows someone, the person can't be a judge
                candidates[e[0]] = -1
                if len(followers[e[1]]) == N:
                    judge = e[1]
                if judge not in candidates:
                    judge = -1
        return judge

N = int(read().rstrip())
temp = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
trust = []
for e in temp:
    trust.append(list(map(int,e.split(','))))

mod = Solution()
print(mod.findJudge(N, trust))
