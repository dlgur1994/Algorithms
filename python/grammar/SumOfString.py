numOfNumber = int(input())
numBefore = input()
sum = 0
for i in range(numOfNumber):
    sum += int(numBefore[-i-1])

print(sum)
