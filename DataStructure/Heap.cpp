#include <iostream>
#include <vector>
#include <array>

using namespace std;

class Heap {
private:
    vector<int> heap;
    int parent;
    int child;
public:
    Heap() {
        heap.assign(1,0);
    }

    void pushValue(int val) {
        heap.push_back(val);
        child = heap.size()-1;
        parent = child/2;
        while(heap[parent] < heap[child]) {
            heap[0] = heap[child];
            heap[child] = heap[parent];
            heap[parent] = heap[0];
            child = parent;
            parent = child/2;
        }
    }

    void printValues() {
        for (int i=1 ; i<heap.size() ; i++) {
            cout << heap[i] << ' ';
        }
        cout << endl;
    }

    int popValue() {
        int ret_val = heap[1];
        int child2, bigger;
        heap[1] = heap[heap.size()-1];
        heap.pop_back();
        parent = 1;
        while(parent < heap.size()) {
            child = parent*2;
            child2 = parent*2+1;
            cout << child << ' ' << child2 << endl;
            bigger = (heap[child] > heap[child2])? child : child2;
            if (heap[parent] < heap[bigger]) {
                heap[0] = heap[bigger];
                heap[bigger] = heap[parent];
                heap[parent] = heap[0];
            }
            parent = bigger;
        }
        return ret_val;
    }
};

int main(void) {
    array<int,10> values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    Heap heap;
    for (int i=0 ; i<values.size() ; i++) {
        heap.pushValue(values[i]);
    }
    heap.printValues();

    cout << heap.popValue() << " Erased" << endl;
    heap.printValues();

    return 0;
}