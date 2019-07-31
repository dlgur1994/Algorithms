def drawHanoi(num,start,mid,end):
    if(num==1):
        print(start, end)
    else:
        drawHanoi(num-1,start,end,mid)
        print(start, end)
        drawHanoi(num-1,mid,start,end)

def getHanoi(num):
    if(num==1):
        return 1
    else:
        return 1+2*getHanoi(num-1)

numOfPlates = int(input())
print(getHanoi(numOfPlates))
drawHanoi(numOfPlates,1,2,3)
