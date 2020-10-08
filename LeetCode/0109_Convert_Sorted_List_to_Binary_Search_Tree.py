import sys
read = sys.stdin.readline

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertNode(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail = self.tail.next
    def printNode(self):
        self.cur = self.head
        while self.cur:
            print(self.cur.val)
            self.cur = self.cur.next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printNode(root):
    if root.left.val == None:
        output.append('Null')
    if root.right.val == None:
        output.append('Null')
    output.append(root.left.val)
    output.append(root.right.val)
    printNode(root.left)
    printNode(root.right)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getValues(head):
            temp = []
            while head:
                temp.append(head.val)
                head = head.next
            return temp
        def makeTree(values,low,high):
            if low>high:
                return
            mid = (low+high)//2
            new_node = TreeNode(values[mid])
            new_node.left = makeTree(values,low,mid-1)
            new_node.right = makeTree(values,mid+1,high)
            return new_node

        value_list = getValues(head)
        return makeTree(value_list,0,len(value_list)-1)

input = list(read().rstrip().lstrip('[').rstrip(']').split(','))
linked_list = LinkedList()
for e in input:
    linked_list.insertNode(int(e))

mod = Solution()
output = [mod.sortedListToBST(linked_list.head).val]
printNode(mod.sortedListToBST(linked_list.head))
print(output)
