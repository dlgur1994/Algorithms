def addNumbers(v1, v2):
    return v1+v2
def changeNumbers(v1, v2):
    return v2, v1

num1 = 10
num2 =20
print(addNumbers(num1,num2))
print(changeNumbers(num1,num2))

lambdaMulti = lambda v1,v2 : v1*v2
print(lambdaMulti(num1,num2))
