listTest = [1,2,3,4]

print(listTest)
print(listTest[2])
print(listTest[1:4])
print(listTest*3)
print(listTest+listTest)

listTest = list(range(1,21,3))
print(listTest)
print(4 in listTest, 5 in listTest)

listTest.append(99)
print(listTest)
listTest.remove(13)
print(listTest)
listTest.reverse()
print(listTest)
listTest.sort()
print(listTest)
