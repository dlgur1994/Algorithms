import sys
read = sys.stdin.readline

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def printNode(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        for i in range(b): # Point to ptr1 and ptr2 at each front of a and b.
            if i == a-1:
                ptr1 = cur
            cur = cur.next
        ptr2 = cur.next
        ptr1.next = list2 # Connect the following from ptr1 to list2.
        while ptr1.next: # Go to the last node of the connected list2.
            ptr1 = ptr1.next
        ptr1.next = ptr2 # Connect the rest of list1 to its most end node.
        return list1

values1 = list(map(int, read().rstrip().split(',')))
a, b = map(int, read().rstrip().split(','))
values2 = list(map(int, read().rstrip().split(',')))
linked_list1 = LinkedList()
linked_list2 = LinkedList()
for value in values1:
    linked_list1.insertNode(ListNode(value))
for value in values2:
    linked_list2.insertNode(ListNode(value))
# linked_list1.printNode()
# linked_list2.printNode()

mod = Solution()
head = mod.mergeInBetween(linked_list1.head, a, b, linked_list2.head)
while head:
    print(head.val)
    head = head.next
