class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        dummy = Node('dummy')
        self.head = dummy
        self.tail = dummy

    def insertNode(self,data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode

    def printList(self):
        cur = self.head
        while cur != self.tail.next:
            print(cur.data)
            cur = cur.next

    def searchNode(self,find_data):
        cur = self.head
        while cur != self.tail.next:
            if(cur.data == find_data):
                print('found')
                return
            cur = cur.next
        print('not found')

    def deleteNode(self,delete_data):
        cur = self.head
        while cur != self.tail.next:
            if(cur.next.data == delete_data):
                cur.next = cur.next.next
                return
            cur = cur.next


linkedList = LinkedList()
linkedList.insertNode(3)
linkedList.insertNode(4)
linkedList.insertNode(5)
linkedList.insertNode(6)
linkedList.printList()

linkedList.searchNode(3)
linkedList.searchNode(4)
linkedList.searchNode(5)
linkedList.searchNode(6)
linkedList.searchNode(7)

linkedList.deleteNode(3)
linkedList.deleteNode(4)
linkedList.deleteNode(5)
linkedList.deleteNode(6)
linkedList.printList()
