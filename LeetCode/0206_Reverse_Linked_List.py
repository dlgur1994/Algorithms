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
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        for i in range(1,len(node_list)-1):
            node_list[-i].next = node_list[-i-1]
        node_list[0].next = None
        return node_list[-1]

input_list = list(map(int,read().rstrip().split(',')))
linked_list = LinkedList()
for e in input_list:
    linked_list.insertNode(ListNode(e))
mod = Solution()
print(mod.reverseList(linked_list.head))
