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

    def printNode(self, node):
        print(node.val)
        if node.next:
            self.printNode(node.next)

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        nodes = []
        cur = head
        while cur != None: # store all nodes in the list
            nodes.append(cur)
            cur = cur.next
        nodes[k-1].val, nodes[len(nodes)-k].val = nodes[len(nodes)-k].val, nodes[k-1].val # swap the value of the corresponding location nodes
        return head

vals = list(map(int, read().rstrip().split(',')))
k = int(read().rstrip())
linked_list = LinkedList()
for val in vals:
    linked_list.insertNode(ListNode(val))
linked_list.printNode(linked_list.head)
mod = Solution()
head = mod.swapNodes(linked_list.head, k)
while head != None:
    print(head.val)
    head = head.next
