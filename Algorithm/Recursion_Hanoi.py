def hanoitower(numOfBlock,a,b,c):
    if (numOfBlock==1):
        return blockList.append([a,c])
    else:
        hanoitower(numOfBlock-1,a,c,b)
        blockList.append([a,c])
        hanoitower(numOfBlock-1,b,a,c)
    return blockList

input = int(input())
blockList = []
result = hanoitower(input,1,2,3)
print(len(result))
print(result)
