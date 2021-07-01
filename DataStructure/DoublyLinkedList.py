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

    def insert_node(self,insert_data):
        newNode = Node(insert_data)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def search_node(self,search_data):
        cur = self.head
        while cur != self.tail.next:
            if(cur.data == search_data):
                print('found')
                return
            cur = cur.next
        print('not found')

    def delete_node(self,delete_data):
        cur = self.head
        while cur != self.tail.next:
            if(cur.next.data == delete_data):
                if cur.next == self.tail:
                    self.tail = cur
                    return
                cur.next = cur.next.next
                cur.next.prev = cur
                return
            cur = cur.next

    def print_node(self):
        cur = self.head
        while cur != self.tail.next:
            print(cur.data)
            cur = cur.next

    def print_node_reverse(self):
        cur = self.tail
        while cur != self.head.prev:
            print(cur.data)
            cur = cur.prev

doublyLinkedList = DoublyLinkedList()
doublyLinkedList.insert_node(3)
doublyLinkedList.insert_node(4)
doublyLinkedList.insert_node(5)
doublyLinkedList.print_node()
doublyLinkedList.print_node_reverse()

doublyLinkedList.search_node(3)
doublyLinkedList.search_node(4)
doublyLinkedList.search_node(5)

doublyLinkedList.delete_node(3)
doublyLinkedList.delete_node(4)
doublyLinkedList.delete_node(5)
doublyLinkedList.print_node()
