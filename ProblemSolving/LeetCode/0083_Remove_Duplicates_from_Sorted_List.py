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

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return
        cur = head
        while cur:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return
        check_list = []
        check_list.append(head.val)
        new_head = ListNode(head.val)
        cur = head
        ptr = new_head
        while cur:
            if cur.val not in check_list:
                check_list.append(cur.val)
                ptr.next = ListNode(cur.val)
                ptr = ptr.next
            cur = cur.next
        return new_head
'''

input_list = list(map(int,read().rstrip().split(',')))
linked_list = LinkedList()
for e in input_list:
    linked_list.insertNode(ListNode(e))
mod = Solution()
head = mod.deleteDuplicates(linked_list.head)
while head != None:
    print(head.val)
    head = head.next
