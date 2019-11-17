import sys

num = int(sys.stdin.readline())
numList = []
for _ in range(num):
    numList.append(int(sys.stdin.readline()))

for e in sorted(numList):
    print(e)

#'[]' is faster than 'list()'
#'list.append()' was faster than initializing the list and approaching each component.
