import sys

zeroCount = []
oneCount = []

def fiv():
    zeroCount.append(1)
    oneCount.append(0)
    zeroCount.append(0)
    oneCount.append(1)
    for i in range(2, 41):
        zeroCount.append(zeroCount[i-1]+zeroCount[i-2])
        oneCount.append(oneCount[i-1]+oneCount[i-2])

testCase = int(sys.stdin.readline())
num = []
for i in range(0,testCase):
    num.append(int(sys.stdin.readline()))

fiv()
for i in range(0,testCase):
    print(zeroCount[num[i]],oneCount[num[i]])
