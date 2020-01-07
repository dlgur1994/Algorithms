import sys
read = sys.stdin.readline

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")

input = read()
result = defangIPaddr(input)
print(result, end='')


'''
import sys
read = sys.stdin.readline

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split('.'))

input = read()
result = defangIPaddr(input)
print(result, end='')
'''
