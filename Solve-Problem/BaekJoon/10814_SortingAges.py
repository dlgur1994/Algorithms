import sys

num = int(sys.stdin.readline())
peoList = []
for _ in range(num):
    age,name = sys.stdin.readline().split()
    peoList.append((age,name))

for age,name in sorted(peoList, key = lambda x:int(x[0])):
    print(age, name)
    
#have to make 'age' int
