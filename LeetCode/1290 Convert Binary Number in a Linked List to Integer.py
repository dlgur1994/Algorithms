import sys
read = sys.stdin.readline

class ListNode:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        dummy = ListNode(0)
        self.head = dummy
        self.tail = dummy

    def insert(self,data):
        newNode = ListNode(data)
        self.tail.next = newNode
        self.tail = newNode

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = ''
        while head:
            num += str(head.val)
            head = head.next
        return int(num,2)

numList = list(map(int,read().split(',')))
linkedList = LinkedList()
for e in numList:
    linkedList.insert(e)
mod = Solution()
print(mod.getDecimalValue(linkedList.head))
