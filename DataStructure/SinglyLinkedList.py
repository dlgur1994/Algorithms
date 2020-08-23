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
        while self.head != self.tail.next:
            if(self.head.data == find_data):
                print('found')
                return
            self.head = self.head.next
        print('not found')

    # def deleteNode(self,delete_data):
    #     while self.head != self.tail.next:
    #         if(self.head.next.data == delete_data):
    #             self.head.next = self.head.next.next
    #             return
    #         self.head = self.head.next


linkedList = LinkedList()
linkedList.insertNode(3)
linkedList.insertNode(4)
linkedList.insertNode(5)
linkedList.insertNode(6)
linkedList.printList()
print('w')
linkedList.printList()

# linkedList.searchNode(3)
# linkedList.searchNode(4)
# linkedList.searchNode(5)
# linkedList.searchNode(6)
# linkedList.searchNode(7)


# linkedList.deleteNode(4)
# linkedList.printList()
