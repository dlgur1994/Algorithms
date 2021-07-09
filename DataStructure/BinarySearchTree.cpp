#include <iostream>
#include <array>

using namespace std;

struct Node {
    int data;
    Node * left;
    Node * right;
};

class BinarySearchTree {
private:
    Node * root;

public: 
    BinarySearchTree() {
        root = NULL;
    }

    Node * getHead() {
        return root;
    }

    void insertNode(Node * cur, int val) {
        Node * node = new Node();
        node->data = val;
        node->left = NULL;
        node->right = NULL;

        if (root == NULL) {
            root = node;
            return;
        }

        if (node->data < cur->data) {
            if (cur->left == NULL) {
                cur->left = node;
                return; 
            }
            else { insertNode(cur->left, val); }
        }
        else {
            if (cur->right == NULL) {
                cur->right = node;
                return; 
            }
            else { insertNode(cur->right, val); }
        }
    }

    void printNode(Node * cur) {
        cout << cur->data << ' ';
        if (cur->left != NULL) { printNode(cur->left); }
        if (cur->right != NULL) { printNode(cur->right); }
    }

    void searchNode(Node * cur, int val) {
        if (cur->data == val) {
            cout << "Found" << endl;
            return;
        }
        else if (cur->data > val) {
            if (cur->left != NULL) { searchNode(cur->left, val); }
            else {
                cout << "Not Found" << endl;
                return;
            }            
        }
        else {
            if (cur->right != NULL) { searchNode(cur->right, val); }
            else {
                cout << "Not Found" << endl;
                return;
            }  
        }
    }

    void deleteNode(int val) {
        Node * parent = root;
        Node * child = root;
        while (child != NULL) {
            if (child->data == val) {
                if (child->left==NULL && child->right==NULL) {
                    if (parent->data > child->data) {
                        parent->left = NULL;
                    }
                    else {
                        parent->right = NULL;
                    }
                    cout << val << " Erased (0 child)" << endl;
                    return;
                }
                else if (child->left==NULL) {
                    if (parent->data > child->data) { 
                        parent->left = child->right;
                    }
                    else {
                        parent->right = child->right;
                    }
                    cout << val << " Erased (1 child)" << endl;
                    return;
                }
                else if (child->right==NULL) {
                    if (parent->data > child->data) { 
                        parent->left = child->left;
                    }
                    else {
                        parent->right = child->left;
                    }
                    cout << val << " Erased (1 child)" << endl;
                    return;
                }
                else {
                    Node * cur = child->right;
                    Node * p_cur = child;
                    while(cur->left) {
                        p_cur = cur;
                        cur=cur->left; 
                    }
                    if (parent->data > child->data) { 
                        parent->left = cur;
                        cur->left = child->left;
                        cur->right = child->right;
                    }
                    else {
                        parent->right = cur;
                        cur->left = child->left;
                        cur->right = child->right;
                    }
                    p_cur->left = NULL;
                    cout << val << " Erased (2 children)" << endl;
                    return;
                }
            }
            else if (child->data > val) { 
                parent = child;
                child = child->left;
            }
            else {
                parent = child;
                child = child->right;
            }
        }
        cout << "Not Erased" << endl;
    }
};

int main(void) {
    array<int,10> values = { 4,1,7,5,9,8,2,3,0,6 };
    BinarySearchTree bst;

    for (int i=0 ; i<values.size() ; i++) {
        bst.insertNode(bst.getHead(), values[i]);
    }
    bst.printNode(bst.getHead());
    cout << endl;

    bst.searchNode(bst.getHead(), 8);
    bst.searchNode(bst.getHead(), -1);

    bst.deleteNode(-1);
    
    bst.deleteNode(0);
    bst.printNode(bst.getHead());
    cout << endl;

    bst.deleteNode(2);
    bst.printNode(bst.getHead());
    cout << endl;

    bst.deleteNode(7);
    bst.printNode(bst.getHead());
    cout << endl;

    return 0;
}