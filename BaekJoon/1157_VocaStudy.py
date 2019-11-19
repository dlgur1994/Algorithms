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

    
#longer version
'''
import sys
read = sys.stdin.readline().rstrip

voca = read().upper()
vocaList = list(set(voca))
countList = [0]*len(vocaList)

for e in voca:
    countList[vocaList.index(e)] += 1

if countList.count(max(countList)) == 1:
    print(vocaList[countList.index(max(countList))])
else:
    print('?')
'''
#its length is shorter, but it takes more time.


#shoter version
'''
import sys
read = sys.stdin.readline().rstrip

voca = read().upper()
vocaList = list(set(voca))
countList = []

for e in vocaList:
    countList.append(voca.count(e))
if countList.count(max(countList)) == 1:
    print(vocaList[countList.index(max(countList))])
else:
    print('?')
'''
#it takes shorter time

#best versiont
'''
import sys

voca = sys.stdin.readline().rstrip().upper()
vocaList = list(set(voca))
countList = []

for e in vocaList:
    countList.append(voca.count(e))
if countList.count(max(countList)) == 1:
    print(vocaList[countList.index(max(countList))])
else:
    print('?')
'''
#When there's only one input, it is better not to use 'read=sys.stdin.readline'
