numTestCast = int(input())
for i in range(numTestCast):
    temp = list(map(int, input().split()))
    numStudent = temp[0]

    listScore = [0]*numStudent
    sum = 0;
    count = 0;
    for j in range(numStudent):
        listScore[j] = temp[j+1]
        sum = sum+listScore[j]
    average = sum/numStudent

    for j in range(numStudent):
        if(listScore[j]>average):
            count = count+1
    percent = count/numStudent*100
    print('%0.3f%%' %percent)
