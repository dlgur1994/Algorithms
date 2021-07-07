#include <iostream>
#include <array>

using namespace std;

struct Node {
    int data;
    Node * left;
    Node * right;
};

class BinaryTree {
private:
    Node * root;

public:
    BinaryTree() {
        root = NULL;    
    }

    Node * getRoot() {
        return root;
    }

    void addNode(Node * cen_node, Node * left_node, Node * right_node) {
        if (root == NULL) { root = cen_node; }
        cen_node->left = left_node;
        cen_node->right = right_node;
    }

    // center -> left -> right
    void preorder(Node * cur) {
        cout << cur->data << ' ';
        if (cur->left != NULL) { preorder(cur->left); }
        if (cur->right != NULL) { preorder(cur->right); }
    }

    // left -> center -> right
    void inorder(Node * cur) {
        if (cur->left != NULL) { inorder(cur->left); }
        cout << cur->data << ' ';
        if (cur->right != NULL) { inorder(cur->right); }
    }

    // left -> right -> center
    void postorder(Node * cur) {
        if (cur->left != NULL) { postorder(cur->left); }
        if (cur->right != NULL) { postorder(cur->right); }
        cout << cur->data << ' ';
    }
};

int main(void) {
    array<int,9> values = {0, 1, 2, 3, 4, 5, 6, 7, 8};
    array<Node *,9> nodes = {};
    for (int i=0 ; i<values.size() ; i++) {
        Node * new_node = new Node();
        new_node->data = values[i];
        new_node->left = NULL;
        new_node->right = NULL;
        nodes[i] = new_node;
    }

    BinaryTree binarytree;
    for (int i=0 ; i<nodes.size()/2 ; i++) {
        binarytree.addNode(nodes[i], nodes[2*i+1], nodes[2*i+2]);
    }

    binarytree.preorder(binarytree.getRoot());
    cout << endl;
    binarytree.inorder(binarytree.getRoot());
    cout << endl;
    binarytree.postorder(binarytree.getRoot());
    cout << endl;

    return 0;
}