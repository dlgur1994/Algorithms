import sys

num = int(sys.stdin.readline())
peoDict = list()
for _ in range(num):
    age,name = sys.stdin.readline().split()
    peoDict.append((age,name))

for age,name in sorted(peoDict, key = lambda x:int(x[0])):
    print(age, name)

#have to make 'age' int.
