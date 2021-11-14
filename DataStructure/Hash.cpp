#include <iostream>
#include <array>
#include <vector>
#include <list>

using namespace std;

template <typename T>
class HashTable {
private:
    int hash_size;
    vector<list<T> > hash_table;

public:
    HashTable(int size) {
        hash_size = size;
        hash_table(hash_size, NULL);
    }
    
    // int hashing(T val) {
    //     return (val)%hash_size;
    // }
    
    // void InsertData(T val) {
    //     // hash_table[hashing(val)].push_back(val);
    //     cout << hashing(val) << endl;
    // }

    // void PrintData() {
    //     list<T>::iterator iter;
    //     for (int i=0 ; i<hash_size ; i++) {
    //         cout << "Key " << i << ": " << endl;
    //         for (iter=hash_table[i].begin() ; iter!=hash_table[i].end(); iter++) {
    //             cout << *iter << " ";
    //         }
    //         cout << endl;
    //     }
    // }

    void DeleteData(T val) {}
    void SearchData(T val) {}
};


int main(void) {
    array<int,10> values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    HashTable<list<int> > hash_table(5);
    // for (int i=0 ; i<values.size() ; i++) {
    //     hash_table.InsertData(values[i]);
    // }
    // hash.PrintData();


    return 0;
}