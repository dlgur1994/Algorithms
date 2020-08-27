class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        dummy = Node('dummy')
        self.head = dummy
        self.tail = dummy

    def insertNode(self,data):
        newNode = Node(data)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def searchNode(self,data):
        cur = self.head
        while cur != self.tail.next:
            if(cur.data == data):
                print('found')
                return
            cur = cur.next
        print('not found')

    def printNode(self):
        cur = self.head
        while cur != self.tail.next:
            print(cur.data)
            cur = cur.next

    def printNodeReverse(self):
        cur = self.tail
        while cur != self.head.prev:
            print(cur.data)
            cur = cur.prev

doublyLinkedList = DoublyLinkedList()
doublyLinkedList.insertNode(3)
doublyLinkedList.insertNode(4)
doublyLinkedList.insertNode(5)
# doublyLinkedList.printNode()
doublyLinkedList.printNodeReverse()

# doublyLinkedList.searchNode(3)
# doublyLinkedList.searchNode(4)
# doublyLinkedList.searchNode(5)
