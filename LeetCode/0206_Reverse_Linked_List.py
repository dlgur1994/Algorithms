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
            return
        self.cur = self.head
        while self.cur.next != None:
            self.cur = self.cur.next
        self.cur.next = node
    def printNode(self):
        self.cur = self.head
        while self.cur != None:
            print(self.cur.val)
            self.cur = self.cur.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        values = []
        while head:
            values.append(head.val)
            head = head.next
        new_head = ListNode(values[-1])
        cur = new_head
        for i in range(len(values)-2,-1,-1):
            cur.next = ListNode(values[i])
            cur = cur.next
        return new_head

input_list = list(map(int,read().rstrip().split(',')))
linked_list = LinkedList()
for e in input_list:
    linked_list.insertNode(ListNode(e))
mod = Solution()
head = mod.reverseList(linked_list.head)
while head != None:
    print(head.val)
    head = head.next
