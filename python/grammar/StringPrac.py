str = "Hello world! How are you?"
strcopy = "Hello world! How are you?"

print(str)
print(str[0])
print(str[1])
print(str[-1])
print(str[-2])
print(len(str))

print(strcopy, str==strcopy)
print(str*2)
print(str + " " + "I'm good")

print("How" in str)
print("Hello" not in str)

print(str[1:len(str):2])
print(str[5::-2])
