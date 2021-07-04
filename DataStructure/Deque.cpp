#include <iostream>
#include <array>

using namespace std;

struct Node {
    int data;
    Node * next;
};

class Deque {
private:
    Node * head;
    Node * tail;
    Node * node;
    Node * cur;
    int pop_val;

public:
    Deque() {
        head = NULL;
        tail = NULL;
    }

    bool isEmpty() {
        if (head==NULL || tail==NULL) { return true; }
        else { return false; }
    }

    void pushFront(int val) {
        node = new Node();
        node->data = val;
        node->next = NULL;
        if (isEmpty()) {
            head = node;
            tail = node;
        }
        else {
            node->next = head;
            head = node;
        }
    }

    void pushBack(int val) {
        node = new Node();
        node->data = val;
        node->next = NULL;
        if (isEmpty()) {
            head = node;
            tail = node;
        }
        else {
            tail->next = node;
            tail = node;
        }
    }

    int popFront() {
        if (isEmpty()) {
            cout << "Empty" << endl;
            return -1;
        }
        pop_val= head->data;
        cur = head;
        head = head->next;
        delete cur;
        return pop_val;
    }
    
    int popBack() {
        if (isEmpty()) {
            cout << "Empty" << endl;
            return -1;
        }
        pop_val= tail->data;
        cur = head;
        while(cur->next != tail) { cur = cur->next; }
        tail = cur;
        tail->next = NULL;
        cur = cur->next;
        delete cur;
        return pop_val;
    }

    void printElements() {
        if (isEmpty()) {
            cout << "Empty" << endl;
            return;
        }
        cur = head;
        while(cur != tail->next) {
            cout << cur->data << ' ';
            cur = cur->next;
        }
        cout << endl;
    }
};

int main(void) {
    array<int,5> values = {1,2,3,4,5};
    Deque deque;

    for (int i=0 ; i<values.size() ; i++) {
        if (i > 2) { deque.pushFront(values[i]); }
        else {deque.pushBack(values[i]);}
    }
    deque.printElements();

    cout << deque.popFront() << endl;
    cout << deque.popBack() << endl;
    deque.printElements();

    cout << deque.popFront() << endl;
    cout << deque.popBack() << endl;
    cout << deque.popFront() << endl;
    deque.printElements();

    cout << deque.popBack() << endl;
    deque.printElements();

    return 0;
}