str = input().split('-')
result = 0

for i in range(0, len(str)):
    str[i] = sum(map(int,str[i].split('+')))
    if(i == 0):
        result += str[i]
    else:
        result -= str[i]

print(result)
