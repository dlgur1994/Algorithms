#include <iostream>

using namespace std;

int main(void) {
    int nums[9];
    int max=0 ,idx=0;

    for (int i=0 ; i<9 ; i++) {
        cin >> nums[i];
    }
    for (int i=0 ; i<9 ; i++) {
        if (nums[i] > max) {
            max = nums[i];
            idx = i;
        } 
    }

    cout << max << "\n" << idx+1 << "\n";
    return 0;
}