import sys
read = sys.stdin.readline

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")

ipadd = Solution()
input = read()
result = ipadd.defangIPaddr(input)
print(result, end='')


'''
import sys
read = sys.stdin.readline

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split('.'))

ipadd = Solution()
input = read()
result = ipadd.defangIPaddr(input)
print(result, end='')
'''
