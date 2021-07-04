#include <iostream>
#include <array>

using namespace std;

struct Node {
    int data;
    Node * next;
};

class Queue {
private:
    Node * head;
    Node * tail;
    Node * node;
    Node * cur;
    int pop_val;

public:
    Queue() {
        head = NULL;
        tail = NULL;
    }

    void push(int val) {
        node = new Node();
        node->data = val;
        node->next = NULL;
        if (head==NULL && tail==NULL) { 
            head = node; 
            tail = node;
        }
        else {
            tail->next = node;
            tail = tail->next;
        }
    }

    int pop() {
        pop_val = head->data;
        cur = head;
        head = head->next;
        delete cur;
        return pop_val;
    }

    void printElement() {
        cur = head;
        while (cur != tail->next) {
            cout << cur->data << ' ';
            cur = cur->next;
        }
        cout << endl;
    }
};

int main(void) {
    array <int,5> values = {1,2,3,4,5};
    Queue queue;

    for (int i=0 ; i<values.size() ; i++) {
        queue.push(values[i]);
    }
    queue.printElement();
    cout << queue.pop() << endl;
    cout << queue.pop() << endl;
    queue.printElement();
    cout << queue.pop() << endl;
    cout << queue.pop() << endl;
    cout << queue.pop() << endl;
    queue.printElement();

    return 0;
}