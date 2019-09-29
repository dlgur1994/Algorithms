numOfTask = int(input())
table = [0]*(numOfTask+1)

for i in range(0,numOfTask):
    day,ramen = map(int,input().split())
    table[day] = max(table[day],ramen)

result = sum(table)
print(result)
print(table)
