def main():
    num1 = 20
    num2 = 10
    numPlus = num1+num2
    numMinus = num1-num2
    numMultiply = num1*num2
    numDivide = num1/num2
    numRemainder = num1%num2

    print(numPlus, numMinus, numMultiply, numDivide, numRemainder)

    num2, num1 = num1, num2
    print(num1,num2)
    print("%d, %d, %d, %d, %d" % ((num1+num2),(num1-num2),(num1*num2),(num1/num2),(num1%num2)))

main()
