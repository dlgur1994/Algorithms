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
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def printNode(self):
        cur = self.head
        while cur != None:
            print(cur.val)
            cur = cur.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        cur = head
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1 == None: cur.next = l2
        if l2 == None: cur.next = l1
        return head

input_list1 = read().rstrip().split(',')
input_list2 = read().rstrip().split(',')
linked_list1 = LinkedList()
linked_list2 = LinkedList()
for e in input_list1:
    linked_list1.insertNode(ListNode(e))
for e in input_list2:
    linked_list2.insertNode(ListNode(e))
mod = Solution()
head = mod.mergeTwoLists(linked_list1.head, linked_list2.head)
while head != None:
    print(head.val)
    head = head.next
