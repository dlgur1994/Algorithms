def checkPrimes(v):
    for i in range(2,v):
        if v%i == 0:
            return False
    return True

def findPrimes(v1,v2):
    count = 1
    for i in range(v1,v2):
        if checkPrimes(i) == True:
            print(i," is ",count,"th prime number.")
            count = count+1

findPrimes(1,10)
