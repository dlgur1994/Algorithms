#include <stdio.h>

struct Node {
    int val;
    Node * next;
};

class LinkedList {
private: 
public:
    // void addNode(Node * head, Node * tail, int val) {
    //     Node * ptr = new Node();
    //     ptr->val = val;
    //     ptr->next = NULL;
    //     if (head == NULL) {
    //         head = ptr;
    //     }
    //     else {
    //         tail->next = ptr;
    //     }
    //     tail = ptr; 
    // }

    void searchNode(Node * cur, Node * tail, int target) {
        int id = 0;
        bool flag = false;
        while (cur != tail->next) {
            if (cur->val == target) {
                printf("target index: %d\n", id);
                flag = true;
                break;
            }
            cur = cur->next;
            id++;
        }
        if (flag == false) {
            printf("can't find value\n");
        }
    }

    void printNode(Node * cur, Node * tail) {
        while (cur != tail->next) {
            printf("%d ", cur->val);
            cur = cur->next;
        }
        printf("\n");
    }

};

int main(void) {
    LinkedList linked_list;
    int values[5] = {1, 2, 3, 4, 5};
    Node * head = NULL;
    Node * tail = NULL;
    Node * cur = NULL;
    
    for (int i=0 ; i<5 ; i++){
        // linked_list.addNode(head, tail, values[i]);
        Node * ptr = new Node();
        ptr->val = values[i];
        ptr->next = NULL;
        if (head == NULL) {
            head = ptr;
        }
        else {
            tail->next = ptr;
        }
        tail = ptr;
    }

    linked_list.searchNode(head, tail, 5);
    linked_list.searchNode(head, tail, 6);
    linked_list.printNode(head, tail);
 
    return 0;
}