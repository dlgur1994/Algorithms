import sys
read = sys.stdin.readline

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insertNode(self,node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = head
        pre = ListNode('dummy')
        while cur:
            if cur.val != val:
                pre.next = cur
                pre = pre.next
            cur = cur.next
        return ListNode('dummy').next

input_list = list(map(int,read().rstrip().split(',')))
input_val = int(read().rstrip())
linked_list = LinkedList()
for e in input_list:
    linked_list.insertNode(ListNode(e))
mod = Solution()
head = mod.removeElements(linked_list.head, input_val)
while head:
    print(head.val)
    head = head.next
