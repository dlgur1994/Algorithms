import sys
read = sys.stdin.readline().rstrip

voca = read()
count = {}

voca = voca.upper()
if len(voca)==1:
    print(voca)
    exit()
for e in voca:
    if e not in count:
        count[e] = 1
    else:
        count[e] += 1

countList = sorted(count.items(), key=lambda x:x[1], reverse=True)
if countList[0][1]>countList[1][1]:
    print(countList[0][0])
else:
    print('?')
