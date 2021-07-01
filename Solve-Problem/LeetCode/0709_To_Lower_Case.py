import sys
read = sys.stdin.readline

'''
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
'''

class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(c)+32) if c.isupper() else c for c in str])

sen = read()
mod = Solution()
print(mod.toLowerCase(sen))
