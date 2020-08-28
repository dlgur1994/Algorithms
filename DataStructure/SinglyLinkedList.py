class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        dummy = Node('dummy')
        self.head = dummy
        self.tail = dummy

    def insert_node(self,data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode

    def print_list(self):
        cur = self.head
        while cur != self.tail.next:
            print(cur.data)
            cur = cur.next

    def search_node(self,find_data):
        cur = self.head
        while cur != self.tail.next:
            if(cur.data == find_data):
                print('found')
                return
            cur = cur.next
        print('not found')

    def delete_node(self,delete_data):
        cur = self.head
        while cur != self.tail.next:
            if(cur.next.data == delete_data):
                cur.next = cur.next.next
                return
            cur = cur.next


linkedList = SinglyLinkedList()
linkedList.insert_node(3)
linkedList.insert_node(4)
linkedList.insert_node(5)
linkedList.insert_node(6)
linkedList.print_list()

linkedList.search_node(3)
linkedList.search_node(4)
linkedList.search_node(5)
linkedList.search_node(6)
linkedList.search_node(7)

linkedList.delete_node(3)
linkedList.delete_node(4)
linkedList.delete_node(5)
linkedList.delete_node(6)
linkedList.print_list()
