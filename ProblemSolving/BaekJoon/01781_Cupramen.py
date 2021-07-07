import sys
read = sys.stdin.readline

numOfTask = int(read())
table = [0]*(numOfTask+1)

for i in range(0,numOfTask):
    day,ramen = map(int,read().split())
    table[day] = max(table[day],ramen)

result = sum(table)
print(result)
print(table)
