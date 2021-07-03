#include <iostream>
#include <array>

using namespace std;

class Stack {
private:
    int top, maxsize;
    int * stack;
public:
    Stack(int size) {
        top = -1;
        maxsize = size;
        stack = new int[maxsize];
    }

    bool isEmpty() {
        if (top == -1){ return true; }
        else { return false; }
    }

    bool isFull() {
        if (top == maxsize-1) { return true; }
        else { return false; }
    }

    void push(int val) {
        if (isFull()) {
            cout << "Full" << endl;
            return;
        }
        else { stack[++top] = val; }
    }

    int pop() {
        return stack[top--];
    }
    
    void searchVal(int val) {
        for (int i=0 ; i<top ; i++) {
            if (stack[i] == val) {
                cout << "index: " << i << endl;
                return;
            }
        }
        cout << "Not found" << endl;
    }

    void printVal() {
        for (int i=0 ; i<top+1 ; i++) {
            cout << stack[i] << ' ';
        }
        cout << endl;
    }
};

int main(void) {
    array <int,5> values = {1,2,3,4,5};
    Stack stack(values.size());

    for (int i=0 ; i<values.size() ; i++) {
        stack.push(values[i]);
    }

    cout << stack.isEmpty() << endl;
    cout << stack.isFull() << endl;
    stack.printVal();
    cout << stack.pop() << endl;
    stack.searchVal(2);
    stack.searchVal(6);
    cout << stack.isEmpty() << endl;
    cout << stack.isFull() << endl;

    return 0;
}