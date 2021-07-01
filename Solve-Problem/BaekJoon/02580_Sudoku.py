import sys

arr = [[]*9 for i in range(9)]
for i in range(9):
    arr[i] = list(map(int,sys.stdin.readline().split()))

while(True):
    count = 0
    for i in range(9):
        count = count+arr[i].count(0)
    if(count==0):
        break

    #가로줄
    for i in range(9):
        addTemp = 0
        if(arr[i].count(0)==1):
            for j in range(9):
                if(arr[i][j]!=0):
                    addTemp = addTemp + arr[i][j]
                else:
                    jTemp = j
            arr[i][jTemp] = 45-addTemp

    #세로줄
    for i in range(9):
        count = 0
        addTemp = 0
        for j in range(9):
            addTemp = addTemp + arr[j][i]
            if(arr[j][i]==0):
                count = count+1
                jTemp = j
                if(count>1):
                    break
        if(count==1):
            arr[jTemp][i] = 45-addTemp

    #9칸씩
    for i in range(3):
        j=1
        for j in range(3):
            addTemp = 0
            iTemp = 0
            jTemp = 0
            for k in range(3):
                for p in range(3):
                    addTemp = addTemp + arr[3*i+k][3*j+p]
                    if(arr[3*i+k][3*j+p]==0):
                        iTemp = 3*i+k
                        jTemp = 3*j+p
            if(addTemp != 45):
                arr[iTemp][jTemp] = 45-addTemp

for i in range(9):
    for j in range(9):
        print(arr[i][j], end=' ')
    print('')
